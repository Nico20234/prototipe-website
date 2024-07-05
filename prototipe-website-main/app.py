from flask import Flask, render_template, jsonify
import mysql.connector

app = Flask(__name__)

def get_db_connection():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="tu_base_de_datos"  # Cambia esto por el nombre de tu base de datos
    )
    return connection

@app.route('/')
def index():
    return render_template('checkout.html')

@app.route('/get_clients')
def get_clients():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute('SELECT id, email FROM clientes')  # Cambia "clientes" por el nombre de tu tabla
    clients = cursor.fetchall()
    cursor.close()
    connection.close()
    return jsonify(clients)

if __name__ == '__main__':
    app.run(debug=True)
