import notas.nota as modelo

class Acciones:

    def crear(self,usuario):
        print(f"ok {usuario[1]} vamos a crear una nueva nota...")
        titulo=input("INTRODUCE EL TITULO DE TU NOTA: ")
        descripcion=input("Describe tu nota... ")

        nota=modelo.nota(usuario[0],titulo,descripcion)
        guardar=nota.GuardarNota()

        if guardar[0]>=1:
            print(f"perfecto tu nota esta almazenada {nota.titulo}")
        
        else: 
            print(f"lo siento no se ha guardado la nota {usuario[1]}")



    def mostrar(self,usuario):
       print(f"\nperfecto {usuario[1]} AQUI TIENES TUS NOTAS: ")
       nota=modelo.nota(usuario[0])
       notas=nota.listar()

       for nota in notas:
           print("\n******************************")
           print(nota[2])
           print(nota[3])

    def borrar(self,usuario):
       print(f"\n ok {usuario[1]}!! VAMOS A BORRAR NOTAS ")

       titulo=input("introduce el titulo de la nota que deseas borrar: ")

       nota=modelo.nota(usuario[0],titulo)
       eliminar=nota.eliminar()

       if eliminar[0]>=1:
        print(f"HEMOS BORRADO LA NOTA {nota.titulo} del sistema")
       else:
        print("No se ha borrado la nota, intenta mas tarde")