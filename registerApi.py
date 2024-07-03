#Conexión a la BD
import mysql.connector

#Flask
from flask import Flask, request, jsonify

#FlaskCors
from flask_cors import CORS

from werkzeug.utils import secure_filename

app = Flask(__name__)
CORS(app)

class Registro:
#----------------------------------------------------------------
# Constructor de la clase

    def __init__(self, host, user, password, database):
        self.conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
        )

        self.cursor = self.conn.cursor()

        try:
            self.cursor.execute(f"USE {database}")
        except mysql.connector.Error as err:
            if err.errno == mysql.connector.errorcode.ER_BAD_DB_ERROR:
                self.conn.database = database
                self.conn.commit()
            else:
                raise err

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios (registerID INT AUTO_INCREMENT PRIMARY KEY, 
        email VARCHAR(255) NOT NULL, 
        password VARCHAR(255) NOT NULL)''')
        self.conn.commit()

        self.cursor.close()
        self.cursor = self.conn.cursor(dictionary=True)

#--------------------------------------------------------------------
# Cuerpo del programa
#--------------------------------------------------------------------

registro = Registro(host='localhost', user='root', password='', database='registro')

def listar_usuarios(self):
    self.cursor.execute("SELECT * FROM usuarios")
    usuarios = self.cursor.fetchall()
    return usuarios

@app.route("/usuarios", methods=["GET"])
def listar_usuarios():
    usuarios = registro.listar_usuarios()
    return jsonify(usuarios)
    
if __name__ == "__main__":
    app.run(debug=True)

def consultar_usuario(self, email):
    self.cursor.execute(f"SELECT * FROM usuarios WHERE email ={email}")
    return self.cursor.fetchone()

def agregar_usuario(self, email, password):
    sql = "INSERT INTO usuarios (email, password) VALUES (%s, %s)"
    valores = (email, password)
    self.cursor.execute(sql, valores)
    self.conn.commit()
    return self.cursor.lastrowid

@app.route("/usuarios", methods=["POST"])
def agregar_usuario():
#Recojo los datos del form
    email = request.form['email']
    password = request.form['password']
    registerID = registro.agregar_usuario(email, password)
    
    if registerID:
        return jsonify({"mensaje": "Usuario registrado correctamente."}), 201
    else:
        return jsonify({"mensaje": "Error al registrar el usuario."}), 500
'''
def modificar_usuario(self, email, nuevo_email, nueva_password):
    sql = "UPDATE usuario SET email = %s, password = %s WHERE email = %s"
    valores = (nuevo_email, nueva_password, email)
    self.cursor.execute(sql, valores)
    self.conn.commit()
    return self.cursor.rowcount > 0

@app.route("/usuarios/<var:email>", methods=["PUT"])
def modificar_usuario(email):
    #Se recuperan los nuevos datos del formulario
    nuevo_email = request.form.get("email")
    nueva_password = request.form.get("password")

    if registro.modificar_usuario(email, nuevo_email, nueva_password):
        return jsonify({"mensaje": "Usuario modificado"}), 200
    else:
        return jsonify({"mensaje": "Usuario no encontrado"}), 403
    

@app.route("/usuarios/<var:email>", methods=["DELETE"])
def eliminar_usuario(email):

    usuario = registro.consultar_usuario()
    if usuario:
        if registro.eliminar_usuario(email):
            return jsonify({"mensaje": "Usuario eliminado"}), 200
        else:
            return jsonify({"mensaje": "Error al eliminar el usuario"}), 500
    else:
        return jsonify({"mensaje": "Usuario no encontrado"}), 404
    
'''
#--------------------------------------------------------------------
if __name__ == "__main__":
    app.run(debug=True)












    
'''
class Registro:
    def __init__(self, host, user, password, database):
        self.conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )

        self.cursor = self.conn.cursor(dictionary=True)
        self.cursor.execute(#CREATE TABLE)
        self.conn.commit()

    def agregar_usuario(self, email, password):
        sql = "INSERT INTO usuarios (email, password) VALUES (%s, %s)"
        valores = (email, password)
        
        self.cursor.execute(sql, valores)
        self.conn.commit()
        return self.cursor.lastrowid
    
    def consultar_usuario(self, email):
        self.cursor.execute(f"SELECT * FROM usuarios WHERE email ={email}")
        return self.cursor.fetchone()
    
# Modificamos un usuario de la tabla a partir de su email

    def modificar_usuario(self, email, nuevo_email, nueva_password):
        sql = "UPDATE usuarios SET email = %s, password = %s WHERE email = %s"
        valores = (nuevo_email, nueva_password, email)
        self.cursor.execute(sql, valores)
        self.conn.commit()

# Eliminamos un usuario de la tabla a partir de su email
    def eliminar_usuario(self, email):
        self.cursor.execute(f"DELETE FROM usuarios WHERE email ={email}")
        self.conn.commit()
        return self.cursor.rowcount > 0


registro = Registro(host='localhost', user='root', password='', database='registro')

registro.agregar_usuario('test@test.com', 'test1')
registro.agregar_usuario('nico@test.com', 'pass123')

#registro.modificar_usuario('test@test.com', 'test@test.com','test8')
#registro.eliminar_usuario('test@test.com')
'''