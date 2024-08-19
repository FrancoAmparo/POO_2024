#AQUI ESTAN LOS MENUS DE OPCIONES

from Autos import autos  #importacion de modulos y paquetes
from Clientes import cliente
from Revisiones import revisiones
import getpass
from funciones import * #usamos limpiar pantalla y esperar tecla
from conexionBd import obtener_conexion #conectamos a la bd en algunos momeno

#MENUS DIFERENTES PARA CADA ACCION
def menu_inicial():
    while True:
        limpiarPantalla()
        print("""
             ....::::::Sistema Agencia Autos::::::....
          
          1) Autos
          2) Clientes
          3) Revisiones
          4) Salir
          
        """)
        opcion=input("Eliga una opcion: ").upper()

        if opcion == '1' or opcion == 'AUTOS':
            menu_autos()
            

        elif opcion == '2' or opcion == 'CLIENTES':
            menu_cliente()

        elif opcion == '3' or opcion == 'REVISIONES':
            menu_revisiones()
    

        elif opcion == '4' or opcion == 'SALIR':
            print("¡Que tenga un buen día!...Ha salido del sistema")
            break
        else:
            print("\t Opcion no váida....Porfavor intente de nuevo")
            esperarTecla()


def menu_autos():
    while True:
        limpiarPantalla()
        print("""
        .....:::::¡Gestion Autos!:::::...
          1) Consultar Registros
          2) Insertar Registros
          3) Actualizar Registro
          4) Eliminar Registro
          5) Salir
        """)
        opcion = input("Eliga una opción: ").strip()

        if opcion == '1':
            #CONSULTA
            limpiarPantalla()
            print("¡He aqui todos los registros disponibles!")
            print("")
            #instanciar clases
            obj=autos.Autos(None, None, None, None,None)
            obj.consultar()
            esperarTecla()


        elif opcion == '2':
            #INSERTAR
            limpiarPantalla()
            print("\t\t ¡Registremos un auto!")
            print("")
            print("Ingrese lo que se le pida:")
            matricula=input("Matricula del auto: ")
            marca=input("Marca del auto: ")
            modelo=input("Modelo del auto: ")
            color=input("Color del auto: ")
            nif=input("NIF del cliente(existente): ")
           
            #Crear una instancia de la clase 
            obj=autos.Autos(matricula, marca, modelo, color, nif)
            obj.insertar()
            esperarTecla()
            

        elif opcion == '3':
            #ACTUALIZAR 
            limpiarPantalla()
            print("¡Actualizará registros!")
            print("")
            matricula = input("\tIngrese la matricula del auto a actualizar: ")

            #intancia de clase
            obj=autos.Autos(None, None, None, None,None)
            obj.actualizar(matricula)
            esperarTecla()



        elif opcion == '4':
            #ELIMINAR 
            limpiarPantalla()
            print("Eliminará registros!")
            print("")
            matricula = input("\tIngrese la matricula del auto a eliminar: ")

            #intancia de clase
            obj=autos.Autos(None, None, None, None,None)
            obj.eliminar(matricula)
            esperarTecla()



        elif opcion == '5':

            break
        else:
            print("Opción no válida, intente nuevamente.")
            esperarTecla()





def menu_cliente():
   while True:
        limpiarPantalla()
        print("""
        .....:::::¡Gestion Clientes!:::::...
          1) Consultar Registros
          2) Insertar Registros
          3) Actualizar Registro
          4) Eliminar Registro
          5) Salir
        """)
        opcion = input("Eliga una opción: ").strip()

        if opcion == '1':
            #CONSULTA
            limpiarPantalla()
            print("¡He aqui todos los registros disponibles!")
            print("")
            #instanciar clases
            obj=cliente.Clientes(None, None, None, None,None)
            obj.consultar()
            esperarTecla()


        elif opcion == '2':
            #INSERTAR
            limpiarPantalla()
            print("\t\t ¡Registremos un cliente!")
            print("")
            print("Ingrese lo que se le pida:")
            nombre=input("Nombre cliente: ")
            direccion=input("Dirección cliente: ")
            ciudad=input("Ciudad cliente ")
            tel=input("Teléfono cliente: ")
            
           
            #Crear una instancia de la clase 
            obj=cliente.Clientes(None, nombre, direccion, ciudad, tel)
            obj.insertar()
            esperarTecla()
            

        elif opcion == '3':
            #ACTUALIZAR 
            limpiarPantalla()
            print("¡Actualizará registros!")
            print("")
            nif = input("\tIngrese la NIF del ciente a actualizar: ")

            #intancia de clase
            obj=cliente.Clientes(None, None, None, None,None)
            obj.actualizar(nif)
            esperarTecla()



        elif opcion == '4':
            #ELIMINAR 
            limpiarPantalla()
            print("Eliminará registros!")
            print("")
            nif = input("\tIngrese la NIF del cliente a eliminar: ")

            #intancia de clase
            obj=cliente.Clientes(None, None, None, None,None)
            obj.eliminar(nif)
            esperarTecla()


        elif opcion == '5':

            break
        else:
            print("Opción no válida, intente nuevamente.")
            esperarTecla()



def menu_revisiones():
    while True:
        limpiarPantalla()
        print("""
        .....:::::¡Gestion Revisiones!:::::...
          1) Consultar Registros
          2) Insertar Registros
          3) Actualizar Registro
          4) Eliminar Registro
          5) Salir
        """)
        opcion = input("Eliga una opción: ").strip()

        if opcion == '1':
            #CONSULTA
            limpiarPantalla()
            print("¡He aqui todos los registros disponibles!")
            print("")
            #instanciar clases
            obj=revisiones.Revisiones(None, None, None, None,None, None)
            obj.consultar()
            esperarTecla()


        elif opcion == '2':
            #INSERTAR
            limpiarPantalla()
            print("\t\t ¡Agreguemos una revision nueva!")
            print("")
            print("Ingrese lo que se le pida:")
            cambiofiltro=input("Cambio filtro (S /N): ")
            cambioaceite=input("Cambio aceite (S /N): ")
            cambiofrenos=input("CCambio frenos (S /N) ")
            otro=input("Otra revisión: ")
            matricula=input("Matricula del auto: ")
            
           
            #Crear una instancia de la clase 
            obj=revisiones.Revisiones(None, cambiofiltro, cambioaceite, cambiofrenos, otro, matricula)
            obj.insertar()
            esperarTecla()
            

        elif opcion == '3':
            #ACTUALIZAR 
            limpiarPantalla()
            print("¡Actualizará revisiones!")
            print("")
            no = input("\tIngrese el número de revisión a actualizar: ")

            #intancia de clase
            obj=revisiones.Revisiones(None, None, None, None,None, None)
            obj.actualizar(no)
            esperarTecla()



        elif opcion == '4':
            #ELIMINAR 
            limpiarPantalla()
            print("Eliminará registros!")
            print("")
            no = input("\tIngrese el número de revisión a actualizar: ")

            #intancia de clase
            obj=revisiones.Revisiones(None, None, None, None, None, None)
            obj.eliminar(no)
            esperarTecla()


        elif opcion == '5':

            break
        else:
            print("Opción no válida, intente nuevamente.")
            esperarTecla()









#aqui le dice al pitón que ejecute primero el menu_inicial()
if __name__ == "__main__":
    menu_inicial()


