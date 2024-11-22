from flask import Flask, request, jsonify
from flask_cors import CORS
import MySQLdb
import simplejson
from jose import jwe
from jose.exceptions import JWEError

app = Flask(__name__)
CORS(app)  # Permite que el frontend (Angular) acceda a la API

mydb = MySQLdb.connect(
    host="localhost",
    user="root",
    password="root",
    database="usuariosdb"
)
mycursor = mydb.cursor()

private_key = """-----BEGIN PRIVATE KEY-----
MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQD3VbCtJyZLOtkO
aTrNalCSvnc4rRlMiDRPnnwtjm3yoUFtCmd+qMLgaRvaUaR3Rq2KPmZzO2jM/FNA
fwDJ3sUNdic9qvkKDgPmQtDj2NAuLARNg5QKqPR8jhXxJeYhGlQHWHShBV/B6RFW
x0Of63un5FadF4Xu0JDCGgVBgaW4CewGR7Cyl1Hd4oiyBFvl8SV0Ps1X4nzVBFTD
Pnd1/YQsph4jE+Yy+zS5EiNy8m9H2rprQ3ulJt4xQaWej8rbSBqBE5t/bjWoKL1F
Hm4JSfYBbocq8xoDWc1Z2hdAzrWkQvZZNnN/26pVm1Fisp6T5d7Om6Ahgr4Jsnr0
g6UM91FNAgMBAAECggEADgO/fpg8zb94ZB4nVFNlXGNJex8n01PWbvqCe8xZw4lK
nUSdJ6qlXDTofJ7qrE2HcNFnWbkwj4juqLVplIa4cLJUt+RTtzOjGe2IS5jR9wPM
fJ3rig0XyWT9rkvg9dg5ka778NHOoryznFCvLsUXnSRNmhomnykXQsBZsuQHQV3G
CpOth8F/ky3YSRs14DrkCS6spNYAx5N6Xg6zTc/I9vqgeIw6cwZRBCfOic+G8/ZM
oeCHNMl0De2kzNFGrBlBkp7N8ujkTEHezMWH/2KlBfoDIDFLsBAqTs1HKtxu67HA
MtAfV0/PixdRxhbxERNHPoe7AosJUJic+1dzhjLZEQKBgQD/DlCkj/IexBRy8+yN
1/r++Xem4l00ckZhlHru/jR2LB0fpsXgVE0Vn6YFVUudSScQjVcC3Hggm8LDjhXk
NVoI+WdwFU7nNTPfMn7qnDgC0h7dl0lSx+Izw8CuGfABu1Ct6/3wwWaR38oSfno7
rBXRFRMDZg7GQm2xO7eL++3MtQKBgQD4QA8HwyooVZRaIc/EKoSOo62NR2QmdoJk
Rb/1N1tj6iiWlaApj+aLTIRwdCn0vYD84+Ax9pWFM3yyHvKlX3I1zLjZbtIvc4fo
Va02op/3wsQxyJQJY0EdFlFAm14dV19rKrVPzbd1QdA4jjSnJxLd3FlRd8mZJv5c
31aIs2TpOQKBgQC2bWu6uIaKAN9LdTJeJfwNwSsWv1PA/ndetg/TvxiQ6W6PQ/7G
PCXCcKUTrXVe84KwcReqITz+vcnpi0gXKR3Ty2dzoJoF/2SxoPFsJv5c7iNLhTjZ
r8QYGExJep3S70J+k4vXVs1hSvrCjZop8iTMnlEyHh41KjBBEyBuTGxC/QKBgHsO
FeU9ItqXgVAkTn7orIigLdlIOCawu/XEdWCyLgUa/z+Vr6yqfhcyuLudeWatwRCa
THm3x2odmYQZvyGmbFCqyD5PprSKyiWqwo/AkRcZXnNm/6qfnpkyhNhHq6FTvCK9
Kt8CFBx1oSdHpmXtAncjUMsHW9Ek+RVER/q/IhhRAoGAOwofSLMLjm1HghFg2B0d
EhnoEUl3t3uYR/fAO5wWa30EjsJknB6wdPNiQdHcbsAF/0LzymQbh0+85hs1wwIR
620uwNxVbtIkuZLDo9exvSGf18R9C2LqWlC473qNRbg6YJKb0wo8bSVsxOFvQxSC
NlpzIk/wvdkLySmCn8fwHNc=
-----END PRIVATE KEY-----
"""

def decrypt(data_encrypted):
    item = jwe.decrypt(data_encrypted['data'], private_key)
    item = item.decode("utf-8")
    return simplejson.loads(item)


# Crear usuario
@app.route('/usuarios', methods=['POST'])
def create_usuario():
    print(request.json)
    item = decrypt(request.json)
    print(item)
    sql = "INSERT INTO usuarios (nombre_completo, nombre_usuario, correo, contrasena, telefono) VALUES (%s, %s, %s, %s, %s)"
    val = (item["nombre_completo"], item["nombre_usuario"], item["correo"], item["contrasena"], item["telefono"])
    mycursor.execute(sql, val)
    mydb.commit()
    return jsonify({"id": mycursor.lastrowid})

# Autenticación de usuario
@app.route('/login', methods=['POST'])
def login_usuario():
    item = decrypt(request.json)
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