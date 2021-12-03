"""
PROYECTO PYTHON MYSQL
-ABRIR ASISTENTE QUE PREGUNTE DISTINTAS COSAS 
-PREGUNTAR SI SE QUIERE HACER LOGIN O REGISTRO
-CREAR NOTA, MOSTRAR NOTAS, BORRARLAS
"""
from usuario import acciones


print(""" ESTA ES TU APLICACION DE CONSOLA PAR AGUARDAR NOTAS 
Acciones disponibles:
- Registro
- Login
""")

hazEl=acciones.acciones()  #CREAR OBJETO O INSTANCIAR CLASE
accion=input("Que deseas hacer el dia de hoy:?")

if accion=="Registro"or accion=="registro":
    hazEl.registro()
elif accion=="Login" or accion=="login":
    hazEl.login()


    

