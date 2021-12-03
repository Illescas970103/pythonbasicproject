import usuario.conexion as conexion
import datetime
import hashlib #con este modulo se puede cifrar la contraseña del usuario antes de agregarlo

connect=conexion.conectar()  #ES LA CONEXION A LA BASE DE DATOS 
database=connect[0]
cursor=connect[1]
class usuario:

    def __init__(self,nombre,apellidos,email,password):
        self.nombre=nombre
        self.apellidos=apellidos
        self.email=email
        self.password=password
    
    def registrar(self):
        fecha=datetime.datetime.now()  #en la que se registro el usuario 
        
        #contraseña cifrada 
        cifrado=hashlib.sha256() #SHA ES UN ALGORITMO DE CIFRADO DE CONTRASEÑAS MUY EFECTIVO
        cifrado.update(self.password.encode('utf8')) #SE DEBE DE PASAR LA CONTRASEÑA DE STRINGS A BYTES PARA CIFRAR
        sql="INSERT INTO usuarios VALUES(null,%s,%s,%s,%s,%s)" #para pasarlo a la base de datos
        try:
           usuario=(self.nombre,self.apellidos,self.email,cifrado.hexdigest(),fecha) #se crean tuplas para pasar a sql
           cursor.execute(sql,usuario)
           database.commit()
           result=[cursor.rowcount,self]  # AQUI SE CREA UNA LISTA PARA ENUMERAR SI SE CREO UN NUEVO USUARIO 
        except:
            result=[0,self] #AQUI ES CON BASE A LAS CONDICIONES EN EL METODO USUARIOS
        
        return result

       
    def identificar(self):
        #CONSULTA PARA COMPROBAR SI EXISTE EL USUARIO
        sql="SELECT * FROM usuarios  WHERE email=%s AND password=%s"
        
        #cifrar contraseña

        cifrado=hashlib.sha256()
        cifrado.update(self.password.encode('utf8'))

        #DATOS PARA LA CONSULTA
        usuario=(self.email,cifrado.hexdigest())
        #EJECUCION

        cursor.execute(sql,usuario)
        

        result=cursor.fetchone()

        return result




