from flask import Flask, request, jsonify
from flask_cors import CORS
import MySQLdb
import simplejson

app = Flask(__name__)
CORS(app)  # Permite que el frontend (Angular) acceda a la API

mydb = MySQLdb.connect(
    host="localhost",
    user="root",
    password="root",
    database="usuariosdb"
)
mycursor = mydb.cursor()

# Obtener todos los usuarios
@app.route('/usuarios', methods=['GET'])
def get_all_usuarios():
    mycursor.execute("SELECT * FROM usuarios")
    res = mycursor.fetchall()
    return jsonify(res)

# Obtener usuario por ID
@app.route('/usuarios/<int:id>', methods=['GET'])
def get_usuario_by_id(id):
    mycursor.execute("SELECT * FROM usuarios WHERE id = %s", (id,))
    res = mycursor.fetchone()
    return jsonify(res)

# Crear usuario
@app.route('/usuarios', methods=['POST'])
def create_usuario():
    item = request.json
    sql = "INSERT INTO usuarios (nombre_completo, nombre_usuario, correo, contrasena, telefono) VALUES (%s, %s, %s, %s, %s)"
    val = (item["nombre_completo"], item["nombre_usuario"], item["correo"], item["contrasena"], item["telefono"])
    mycursor.execute(sql, val)
    mydb.commit()
    return jsonify({"id": mycursor.lastrowid})

# Actualizar usuario
@app.route('/usuarios/<int:id>', methods=['PUT'])
def update_usuario(id):
    item = request.json
    sql = """
        UPDATE usuarios 
        SET nombre_completo = %s, nombre_usuario = %s, correo = %s, contrasena = %s, telefono = %s 
        WHERE id = %s
    """
    val = (item["nombre_completo"], item["nombre_usuario"], item["correo"], item["contrasena"], item["telefono"], id)
    mycursor.execute(sql, val)
    mydb.commit()
    return jsonify({"rows_affected": mycursor.rowcount})

# Eliminar usuario
@app.route('/usuarios/<int:id>', methods=['DELETE'])
def delete_usuario(id):
    mycursor.execute("DELETE FROM usuarios WHERE id = %s", (id,))
    mydb.commit()
    return jsonify({"rows_affected": mycursor.rowcount})

# Autenticación de usuario
@app.route('/login', methods=['POST'])
def login_usuario():
    item = request.json
    sql = "SELECT * FROM usuarios WHERE correo = %s AND contrasena = %s"
    val = (item["correo"], item["contrasena"])
    mycursor.execute(sql, val)
    res = mycursor.fetchone()
    if res:
        return jsonify({"status": "success", "usuario": res})
    else:
        return jsonify({"status": "error", "message": "Usuario no encontrado"}), 401

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)