import sys
import os


script_dir = os.path.dirname(__file__)
sys.path.append(script_dir)

from administradores.admin import agregar_administrador, iniciar_sesion
from nomina.nomina import registrar_empleado, ver_salarios
from bonos.bono import asignar_bono
from notificaciones.notificacion import enviar_notificacion, ver_notificaciones

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu_principal():
    while True:
        limpiar_pantalla()
        print("----- Sistema de Nómina Yazaki -----")
        print("1. Agregar Administrador")
        print("2. Iniciar Sesión")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            limpiar_pantalla()
            print("..:::Registro administrador:::..")
            nombre = input("Ingrese el nombre del administrador: ")
            password = input("Cree una contraseña para el administrador: ")
            correo = input("Ingrese el correo del administrador: ")
            admin_id = agregar_administrador(nombre, password, correo)
            print(f"Administrador {nombre} agregado a la base de datos con ID: {admin_id}")
        elif opcion == "2":
            limpiar_pantalla()
            print("..:::Iniciar sesión:::..")
            correo = input("Ingrese el correo del administrador: ")
            password = input("Ingrese la contraseña: ")
            admin = iniciar_sesion(correo, password)
            if admin:
                print("Inicio de sesión exitoso.")
                menu_administrador()
            else:
                print("Credenciales incorrectas.")
        elif opcion == "3":
            break
        else:
            print("Opción no válida. Intente de nuevo.")
        input("Presione Enter para continuar...")

def menu_administrador():
    while True:
        limpiar_pantalla()
        print("----- Menú de Administrador -----")
        print("1. Agregar Empleado")
        print("2. Asignar Bono a Empleado")
        print("3. Ver Salarios")
        print("4. Enviar Notificación")
        print("5. Ver Registro de Notificaciones")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            limpiar_pantalla()
            print("..:::Registro de empleado:::..")
            nombre = input("Ingrese el nombre del empleado: ")
            edad = int(input("Ingrese la edad del empleado: "))
            horas_trabajadas = int(input("Ingrese las horas trabajadas en la semana: "))
            sueldo_dia = float(input("Ingrese el sueldo diario del empleado: "))
            prima_dominical = float(input("Ingrese la prima dominical (%): "))
            tipo_jornada = input("Ingrese el tipo de jornada (Matutina/Vespertina/Nocturna): ")
            dias_trabajados = int(input("Ingrese los días trabajados: "))
            horas_extra = int(input("Ingrese las horas extra trabajadas: "))
            descanso_semanal = input("El empleado descansó en domingo? (Si/No): ").lower() == "si"
            trabajador_id = registrar_empleado(nombre, edad, horas_trabajadas, sueldo_dia, prima_dominical, tipo_jornada, dias_trabajados, horas_extra, descanso_semanal)
            print(f"Empleado {nombre} agregado con ID: {trabajador_id}")
        elif opcion == "2":
            limpiar_pantalla()
            print("..:::Asignación de Bono:::..")
            empleado_id = int(input("Ingrese el ID del empleado: "))
            monto = float(input("Ingrese el monto del bono: "))
            asignar_bono(empleado_id, monto)
            print(f"Bono de ${monto} asignado al empleado con ID: {empleado_id}")
        elif opcion == "3":
            limpiar_pantalla()
            print("..:::Salarios:::..")
            salarios = ver_salarios()
            for salario in salarios:
                print(f"Empleado: {salario[0]}, Salario Base: ${salario[1]}, Bono: ${salario[2]}, Total: ${salario[3]}, Fecha: {salario[4]}")
        elif opcion == "4":
            limpiar_pantalla()
            print("..:::Envío de Notificación:::..")
            empleado_id = int(input("Ingrese el ID del empleado: "))
            mensaje = input("Ingrese el mensaje: ")
            admin_id = input("Ingrese su ID de administrador: ")
            enviar_notificacion(empleado_id, mensaje, admin_id)
            print("Notificación enviada exitosamente.")
        elif opcion == "5":
            limpiar_pantalla()
            print("..:::Registro de Notificaciones:::..")
            notificaciones = ver_notificaciones()
            for notificacion in notificaciones:
                print(f"Mensaje: {notificacion[0]}, Fecha: {notificacion[1]}, Empleado: {notificacion[2]}, Correo Admin: {notificacion[3]}")
        elif opcion == "6":
            break
        else:
            print("Opción no válida. Intente de nuevo.")
        input("Presione Enter para continuar...")

if __name__ == "__main__":
    menu_principal()
