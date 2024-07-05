from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector
from mysql.connector import Error

class Database:
    def __init__(self, host, database, user, password):
        self.conn = mysql.connector.connect(
            host=host,
            database=database,
            user=user,
            password=password
        )
        self.cursor = self.conn.cursor()

    def agregar_usuario(self, email, password):
        sql = "INSERT INTO usuarios (email, password) VALUES (%s, %s)"
        valores = (email, password)
        self.cursor.execute(sql, valores)
        self.conn.commit()
        return self.cursor.lastrowid

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
                host='localhost',  # Reemplazado con 'localhost'
                database='registro',  # Reemplazado con 'registro'
                user='root',  # Reemplazado con 'root'
                password='Titanio0812'  # Reemplazado con 'Titanio0812'
            )
            user_id = db.agregar_usuario(email, password)
            db.cerrar()
            return jsonify({'message': 'Usuario registrado exitosamente', 'user_id': user_id}), 201
        except Error as e:
            print(f"Error: {e}")
            return jsonify({'message': 'Error al registrar el usuario'}), 500
    else:
        return jsonify({'message': 'Solicitud no válida, se esperaba JSON'}), 400

# Ejecutar la aplicación en el puerto 5000
if __name__ == '__main__':
    app.run(debug=True, port=5000)