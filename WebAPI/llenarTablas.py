import MySQLdb

mydb = MySQLdb.connect(
    host="localhost",
    user="root",
    password="root",
    database="usuariosdb"
)

mycursor = mydb.cursor()


def cargarUsuarios():
    usuarios = [
        {
            "nombre_completo": "Antonio Perez",
            "nombre_usuario": "antonio123",
            "correo": "antonio@gmail.com",
            "contrasena": "antonioPass",
            "telefono": "1234567890"
        },
        {
            "nombre_completo": "Maria Lopez",
            "nombre_usuario": "maria321",
            "correo": "maria@gmail.com",
            "contrasena": "mariaPass",
            "telefono": "0987654321"
        }
    ]

    for usuario in usuarios:
        sql = "INSERT INTO usuarios (nombre_completo, nombre_usuario, correo, contrasena, telefono) VALUES (%s, %s, %s, %s, %s)"
        val = (usuario["nombre_completo"], usuario["nombre_usuario"], usuario["correo"], usuario["contrasena"],
               usuario["telefono"])
        mycursor.execute(sql, val)
    mydb.commit()



if __name__ == "__main__":
    cargarUsuarios()
    print("Usuarios cargados exitosamente.")
