
import simplejson

import MySQLdb

mydb = MySQLdb.connect(
    host="localhost",
    user="root",
    password="root",
    database="usuariosdb"
)
mycursor = mydb.cursor()

# Obtener todos los usuarios
def getAllUsuarios():
    mycursor.execute("SELECT * FROM usuarios")
    res = mycursor.fetchall()
    return simplejson.dumps(res)

# Obtener usuario por ID
def getUsuarioById(id):
    mycursor.execute("SELECT * FROM usuarios WHERE id = %s", (id,))
    res = mycursor.fetchone()
    return simplejson.dumps(res)

# Crear usuario
def createUsuario(item):
    sql = "INSERT INTO usuarios (nombre_completo, nombre_usuario, correo, contrasena, telefono) VALUES (%s, %s, %s, %s, %s)"
    val = (item["nombre_completo"], item["nombre_usuario"], item["correo"], item["contrasena"], item["telefono"])
    mycursor.execute(sql, val)
    mydb.commit()
    return mycursor.lastrowid

# Actualizar usuario
def updateUsuario(id, item):
    sql = """
        UPDATE usuarios 
        SET nombre_completo = %s, nombre_usuario = %s, correo = %s, contrasena = %s, telefono = %s 
        WHERE id = %s
    """
    val = (item["nombre_completo"], item["nombre_usuario"], item["correo"], item["contrasena"], item["telefono"], id)
    mycursor.execute(sql, val)
    mydb.commit()
    return mycursor.rowcount

# Eliminar usuario
def deleteUsuario(id):
    mycursor.execute("DELETE FROM usuarios WHERE id = %s", (id,))
    mydb.commit()
    return mycursor.rowcount
