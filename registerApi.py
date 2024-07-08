from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector
from mysql.connector import Error

class Database:
    def __init__(self, host, database, user, password):
        self.conn = mysql.connector.connect(
            host='codoacodojrossi.mysql.pythonanywhere-services.com',
            database='codoacodojrossi$miapp',
            user='codoacodojrossi',
            password='fcy5iZ2CqCOiB6N'
        )
        self.cursor = self.conn.cursor()

    def agregar_usuario(self, email, password):
        sql = "INSERT INTO usuarios (email, password) VALUES (%s, %s)"
        valores = (email, password)
        self.cursor.execute(sql, valores)
        self.conn.commit()
        return self.cursor.lastrowid

    def eliminar_usuario(self, user_id):
        sql = "DELETE FROM usuarios WHERE id = %s"
        self.cursor.execute(sql, (user_id,))
        self.conn.commit()

    def modificar_usuario(self, user_id, email, password):
        sql = "UPDATE usuarios SET email = %s, password = %s WHERE id = %s"
        valores = (email, password, user_id)
        self.cursor.execute(sql, valores)
        self.conn.commit()

    def obtener_usuarios(self):
        sql = "SELECT registerID, email FROM usuarios"
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def cerrar(self):
        self.cursor.close()
        self.conn.close()

app = Flask(__name__)
CORS(app)  # Habilitar CORS en toda la aplicación

@app.route('/usuarios', methods=['POST'])
def register_user():
    if request.is_json:
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')

        # Imprimir los datos para depuración
        print(f"Email: {email}, Password: {password}")

        if not email or not password:
            return jsonify({'message': 'Datos incompletos'}), 400

        try:
            db = Database(
                host='codoacodojrossi.mysql.pythonanywhere-services.com',
                database='codoacodojrossi$miapp',
                user='codoacodojrossi',
                password='fcy5iZ2CqCOiB6N'
            )
            registerID = db.agregar_usuario(email, password)
            db.cerrar()
            return jsonify({'message': 'Usuario registrado exitosamente', 'registerID': registerID}), 201
        except Error as e:
            print(f"Error: {e}")
            return jsonify({'message': 'Error al registrar el usuario'}), 500
    else:
        return jsonify({'message': 'Solicitud no válida, se esperaba JSON'}), 400
    
@app.route('/usuarios/<int:registerID>', methods=['DELETE'])
def delete_user(registerID):
    try:
        db = Database(
            host='codoacodojrossi.mysql.pythonanywhere-services.com',
            database='codoacodojrossi$miapp',
            user='codoacodojrossi',
            password='fcy5iZ2CqCOiB6N'
        )
        sql = "DELETE FROM usuarios WHERE registerID = %s"
        valores = (registerID,)
        db.cursor.execute(sql, valores)
        db.conn.commit()
        db.cerrar()
        return jsonify({'message': 'Usuario eliminado exitosamente'}), 200
    except Error as e:
        print(f"Error: {e}")
        return jsonify({'message': 'Error al eliminar el usuario'}), 500

@app.route('/usuarios/<int:registerID>', methods=['PUT'])
def update_user(registerID):
    if request.is_json:
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')

        if not email or not password:
            return jsonify({'message': 'Datos incompletos'}), 400

        try:
            db = Database(
                host='codoacodojrossi.mysql.pythonanywhere-services.com',
                database='codoacodojrossi$miapp',
                user='codoacodojrossi',
                password='fcy5iZ2CqCOiB6N''
            )
            sql = "UPDATE usuarios SET email = %s, password = %s WHERE registerID = %s"
            valores = (email, password, registerID)
            db.cursor.execute(sql, valores)
            db.conn.commit()
            db.cerrar()
            return jsonify({'message': 'Usuario modificado exitosamente'}), 200
        except Error as e:
            print(f"Error: {e}")
            return jsonify({'message': 'Error al modificar el usuario'}), 500
    else:
        return jsonify({'message': 'Solicitud no válida, se esperaba JSON'}), 400

@app.route('/usuarios', methods=['GET'])
def get_users():
    try:
        db = Database(
            host='codoacodojrossi.mysql.pythonanywhere-services.com',
            database='codoacodojrossi$miapp',
            user='codoacodojrossi',
            password='fcy5iZ2CqCOiB6N'
        )
        usuarios = db.obtener_usuarios()
        db.cerrar()
        return jsonify(usuarios), 200
    except Error as e:
        print(f"Error: {e}")
        return jsonify({'message': 'Error al obtener los usuarios'}), 500


'''# Ejecutar la aplicación en el puerto 5000
if __name__ == '__main__':
    app.run(debug=True, port=5000)'''
