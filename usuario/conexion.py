import mysql.connector

def conectar():
    database=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="master_python",
    port=3306  #ES EL PUERTO POR EL CUAL FUNCIONA EL SERVIDOR DE NUESTRA BASE DE DATOS EN NUESTRO EQUIPO
    )

    cursor=database.cursor(buffered=True)

    return[database,cursor]





#SOLO PARA COMPROBAR SI ESTAS CONECTADO CORRECTAMENTE A LA BASE DE DATOS
print(conectar())

