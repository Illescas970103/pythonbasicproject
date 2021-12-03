import usuario.usuarionuevo as modelo
import notas.acciones

class acciones:
    def registro(self):
        print("\n OK!!, VAMOS A REGISTRARTE CRACK!...")
        nombre=input("¿Cual es tu nombre?: ")
        apellidos=input("¿Cuales son tus apellidos?: ")
        email=input("Introduce una direccion de correo electronico valida: ")
        password=input("Introduce una contraseña para tu login: ")

        usuario=modelo.usuario(nombre,apellidos,email,password)
        registro=usuario.registrar()  #MODELO PARA REGISTRAR AL USUARIO EN LA BASE DE DATOS

        if registro[0]>=1:
            print(f"\n Perfecto {registro[1].nombre} te has registrado con el email {registro[1].email}")
        else:
            print("\n no te has registrado correctamente")

    def login(self):
         print("\nPerfecto, identificate en el sistema PLOX ")
         try:
             email=input("Introduce la direccion de correo electronico que utilizas: ")
             password=input("Introduce una contraseña para tu login: ")

             usuario=modelo.usuario('','',email,password)
             login=usuario.identificar()

             if email==login[3]:
               print(f"bienvenido {login[1]} te has registrado en el sistema el {login[5]}")
               self.proximasAcciones(login)
         except Exception as e:
             print(type(e))
             print(type(e).__name__) # TE INDICA EL TIPO DE ERROR QUE SE GENERA CON EL COMANDO .__name__
             print("login incorrecto intentalo mas tarde ")
    
    def proximasAcciones(self,usuario):
        print(""" 
        -CREAR NOTA (crear)
        -MOSTRAR NOTAS (mostrar)
        -ELIMINAR NOTA(eliminar)
        -SALIR(salir)
        """)

        accion= input("¿Que quieres hacer: ? ")
        haz=notas.acciones.Acciones()

        if accion=="crear":
            haz.crear(usuario)
            self.proximasAcciones(usuario)
        elif accion=="mostrar":
            haz.mostrar(usuario)
            self.proximasAcciones(usuario)
        elif accion== "eliminar":
            haz.borrar(usuario)
            self.proximasAcciones(usuario)
        elif accion=="salir":
            print(f"perfecto {usuario[1]} hasta pronto")
            exit()


        








