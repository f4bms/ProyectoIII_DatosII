import simplejson
from flask import Flask, request, jsonify
from flask_cors import CORS
import dbConection
import mysql.connector

app = Flask(__name__)
app.secret_key = 'clave'
CORS(app)


# Obtener todos los usuarios
@app.route('/usuarios', methods=['GET'])
def get_all_usuarios():
    usuarios = dbConection.getAllUsuarios()
    return jsonify(simplejson.loads(usuarios)), 200


# Obtener usuario por ID
@app.route('/usuarios/<int:id>', methods=['GET'])
def get_usuario(id):
    usuario = dbConection.getUsuarioById(id)
    if usuario:
        return jsonify(simplejson.loads(usuario)), 200
    else:
        return jsonify({"error": "Usuario no encontrado"}), 404


# Crear usuario
@app.route('/usuarios', methods=['POST'])
def create_usuario():
    data = request.get_json()
    required_fields = ["nombre_completo", "nombre_usuario", "correo", "contrasena", "telefono"]

    if not all(field in data for field in required_fields):
        return jsonify({"error": "Todos los campos son obligatorios"}), 400

    try:
        user_id = dbConection.createUsuario(data)
        return jsonify({"message": "Usuario creado exitosamente", "id": user_id}), 201
    except mysql.connector.Error as err:
        return jsonify({"error": str(err)}), 400


# Actualizar usuario por ID
@app.route('/usuarios/<int:id>', methods=['PUT'])
def update_usuario(id):
    data = request.get_json()
    required_fields = ["nombre_completo", "nombre_usuario", "correo", "contrasena", "telefono"]

    if not all(field in data for field in required_fields):
        return jsonify({"error": "Todos los campos son obligatorios"}), 400

    updated_rows = dbConection.updateUsuario(id, data)
    if updated_rows > 0:
        return jsonify({"message": "Usuario actualizado exitosamente"}), 200
    else:
        return jsonify({"error": "Usuario no encontrado"}), 404


# Eliminar usuario por ID
@app.route('/usuarios/<int:id>', methods=['DELETE'])
def delete_usuario(id):
    deleted_rows = dbConection.deleteUsuario(id)
    if deleted_rows > 0:
        return jsonify({"message": "Usuario eliminado exitosamente"}), 200
    else:
        return jsonify({"error": "Usuario no encontrado"}), 404


if __name__ == '__main__':
    app.run(debug=True)
