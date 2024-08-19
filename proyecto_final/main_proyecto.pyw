
import tkinter as tk
from tkinter import messagebox
from administradores.admin import agregar_administrador, iniciar_sesion
from nomina.nomina import registrar_empleado, ver_salarios
from bonos.bono import asignar_bono
from notificaciones.notificacion import enviar_notificacion, ver_notificaciones


def limpiar_pantalla(ventana):
    for widget in ventana.winfo_children():
        widget.destroy()


def ventana_principal():
    ventana = tk.Tk()
    ventana.title("Sistema de Nómina Yazaki")
    ventana.geometry("400x300")

    def mostrar_ventana_principal():
        limpiar_pantalla(ventana)
        tk.Label(ventana, text="..:::::: Sistema de Nómina Yazaki ::::::..", font=("Arial", 30), fg="blue").pack(pady=10)

        tk.Button(ventana, text="Agregar Administrador", command=ventana_agregar_admin, font=("Arial", 20), bg="lightgrey").pack(pady=5)
        tk.Button(ventana, text="Iniciar Sesión", command=ventana_iniciar_sesion,font=("Arial", 20), bg="lightgrey").pack(pady=5)
        tk.Button(ventana, text="Salir", command=ventana.quit,font=("Arial", 20), bg="lightgrey").pack(pady=5)

    def ventana_agregar_admin():
        limpiar_pantalla(ventana)
        tk.Label(ventana, text="..:::Registro administrador:::..", font=("Arial", 30), fg="green").pack(pady=10)
        
        tk.Label(ventana, text="Nombre:", font=("Arial", 20)).pack()
        nombre_entry = tk.Entry(ventana, font=("Arial", 20))
        nombre_entry.pack()

        tk.Label(ventana, text="Contraseña:", font=("Arial", 20)).pack()
        password_entry = tk.Entry(ventana, show='*', font=("Arial", 20))
        password_entry.pack()

        tk.Label(ventana, text="Correo:", font=("Arial", 20)).pack()
        correo_entry = tk.Entry(ventana, font=("Arial", 20))
        correo_entry.pack()

        def registrar_admin():
            nombre = nombre_entry.get()
            password = password_entry.get()
            correo = correo_entry.get()
            admin_id = agregar_administrador(nombre, password, correo)
            messagebox.showinfo("Éxito", f"Administrador {nombre} agregado con ID: {admin_id}")
            mostrar_ventana_principal()

        tk.Button(ventana, text="Registrar", command=registrar_admin, font=("Arial", 20), bg="lightgreen").pack(pady=10)
        tk.Button(ventana, text="Volver", command=mostrar_ventana_principal, font=("Arial", 20), bg="lightcoral").pack()

    def ventana_iniciar_sesion():
        limpiar_pantalla(ventana)
        tk.Label(ventana, text="..:::Iniciar sesión:::..", font=("Arial", 30), fg="orange").pack(pady=10)

        tk.Label(ventana, text="Correo:", font=("Arial", 20)).pack()
        correo_entry = tk.Entry(ventana, font=("Arial", 20))
        correo_entry.pack()

        tk.Label(ventana, text="Contraseña:", font=("Arial", 20)).pack()
        password_entry = tk.Entry(ventana, show='*', font=("Arial", 20))
        password_entry.pack()

        def iniciar():
            correo = correo_entry.get()
            password = password_entry.get()
            admin = iniciar_sesion(correo, password)
            if admin:
                messagebox.showinfo("Éxito", "Inicio de sesión exitoso.")
                ventana_menu_administrador()
            else:
                messagebox.showerror("Error", "Credenciales incorrectas.")
        
        tk.Button(ventana, text="Iniciar Sesión", command=iniciar, font=("Arial", 20), bg="lightblue").pack(pady=10)
        tk.Button(ventana, text="Volver", command=mostrar_ventana_principal, font=("Arial", 20), bg="lightcoral").pack()

    def ventana_menu_administrador():
        limpiar_pantalla(ventana)
        tk.Label(ventana, text="..:::: Menú de Administrador ::::..", font=("Arial", 30), fg="purple").pack(pady=10)
        
        tk.Button(ventana, text="Agregar Empleado", command=ventana_registro_empleado, font=("Arial", 20), bg="lightgrey").pack(pady=5)
        tk.Button(ventana, text="Asignar Bono a Empleado", command=ventana_asignar_bono, font=("Arial", 20), bg="lightgrey").pack(pady=5)
        tk.Button(ventana, text="Ver Salarios", command=ventana_ver_salarios, font=("Arial", 20), bg="lightgrey").pack(pady=5)
        tk.Button(ventana, text="Enviar Notificación", command=ventana_enviar_notificacion, font=("Arial", 20), bg="lightgrey").pack(pady=5)
        tk.Button(ventana, text="Ver Registro de Notificaciones", command=ventana_ver_notificaciones, font=("Arial", 20), bg="lightgrey").pack(pady=5)
        tk.Button(ventana, text="Salir", command=mostrar_ventana_principal, font=("Arial", 20), bg="lightgrey").pack(pady=5)

    def ventana_registro_empleado():
        limpiar_pantalla(ventana)
        tk.Label(ventana, text="..:::Registro de empleado:::..", font=("Arial", 20), fg="teal").pack(pady=10)
        
        campos = ["Nombre", "Edad", "Horas trabajadas", "Sueldo diario", "Prima dominical (%)", "Tipo de jornada", "Días trabajados", "Horas extra", "Descanso en domingo (Si/No)"]
        entries = {}
        
        for campo in campos:
            tk.Label(ventana, text=f"Ingrese {campo.lower()}: ", font=("Arial", 18)).pack()
            entry = tk.Entry(ventana, font=("Arial", 18))
            entry.pack()
            entries[campo] = entry

        def registrar():
            datos = {campo: entry.get() for campo, entry in entries.items()}
            trabajador_id = registrar_empleado(
                datos["Nombre"], int(datos["Edad"]), int(datos["Horas trabajadas"]),
                float(datos["Sueldo diario"]), float(datos["Prima dominical (%)"]),
                datos["Tipo de jornada"], int(datos["Días trabajados"]),
                int(datos["Horas extra"]), datos["Descanso en domingo (Si/No)"].lower() == "si"
            )
            messagebox.showinfo("Éxito", f"Empleado {datos['Nombre']} agregado con ID: {trabajador_id}")
            ventana_menu_administrador()
        
        tk.Button(ventana, text="Registrar", command=registrar, font=("Arial", 20), bg="lightgreen").pack(pady=10)
        tk.Button(ventana, text="Volver", command=ventana_menu_administrador, font=("Arial", 20), bg="lightcoral").pack()

    def ventana_asignar_bono():
        limpiar_pantalla(ventana)
        tk.Label(ventana, text="..:::Asignación de Bono:::..", font=("Arial", 30), fg="darkorange").pack(pady=10)
        
        tk.Label(ventana, text="ID del empleado:", font=("Arial", 20)).pack()
        empleado_id_entry = tk.Entry(ventana, font=("Arial", 20))
        empleado_id_entry.pack()

        tk.Label(ventana, text="Monto del bono:", font=("Arial", 20)).pack()
        monto_entry = tk.Entry(ventana, font=("Arial", 20))
        monto_entry.pack()

        def asignar():
            empleado_id = int(empleado_id_entry.get())
            monto = float(monto_entry.get())
            asignar_bono(empleado_id, monto)
            messagebox.showinfo("Éxito", f"Bono de ${monto} asignado al empleado con ID: {empleado_id}")
            ventana_menu_administrador()
        
        tk.Button(ventana, text="Asignar", command=asignar, font=("Arial", 20), bg="lightgreen").pack(pady=10)
        tk.Button(ventana, text="Volver", command=ventana_menu_administrador, font=("Arial", 20), bg="lightcoral").pack()

    def ventana_ver_salarios():
        limpiar_pantalla(ventana)
        tk.Label(ventana, text="..:::Salarios:::..", font=("Arial", 30), fg="blue").pack(pady=10)
        
        salarios = ver_salarios()
        for salario in salarios:
            tk.Label(ventana, text=f"Empleado: {salario[0]}, Salario Base: ${salario[1]}, Bono: ${salario[2]}, Total: ${salario[3]}", font=("Arial", 20)).pack()

        tk.Button(ventana, text="Volver", command=ventana_menu_administrador, font=("Arial", 20), bg="lightcoral").pack()

    def ventana_enviar_notificacion():
        limpiar_pantalla(ventana)
        tk.Label(ventana, text="..:::Enviar Notificación:::..", font=("Arial", 30), fg="purple").pack(pady=10)
        
        tk.Label(ventana, text="ID del empleado:", font=("Arial", 20)).pack()
        empleado_id_entry = tk.Entry(ventana, font=("Arial", 20))
        empleado_id_entry.pack()

        tk.Label(ventana, text="Mensaje:", font=("Arial", 20)).pack()
        mensaje_entry = tk.Entry(ventana, font=("Arial", 20))
        mensaje_entry.pack()

        tk.Label(ventana, text="ID del administrador:", font=("Arial", 20)).pack()
        admin_id_entry = tk.Entry(ventana, font=("Arial", 20))
        admin_id_entry.pack()



        def enviar():
            empleado_id = int(empleado_id_entry.get())
            mensaje = mensaje_entry.get()
            admin_id = int(admin_id_entry.get())
            enviar_notificacion(empleado_id, mensaje,admin_id)
            messagebox.showinfo("Éxito", f"Notificación enviada al empleado con ID: {empleado_id}")
            ventana_menu_administrador()
        
        tk.Button(ventana, text="Enviar", command=enviar, font=("Arial", 20), bg="lightgreen").pack(pady=10)
        tk.Button(ventana, text="Volver", command=ventana_menu_administrador, font=("Arial", 20), bg="lightcoral").pack()

    def ventana_ver_notificaciones():
        limpiar_pantalla(ventana)
        tk.Label(ventana, text="..:::Registro de Notificaciones:::..", font=("Arial", 30), fg="darkgreen").pack(pady=10)
        
        notificaciones = ver_notificaciones()
        for notificacion in notificaciones:
            
              tk.Label(ventana, text=f"Empleado: {notificacion[2]}, Mensaje: {notificacion[0]}, Fecha: {notificacion[1]}, Administrador: {notificacion[3]}", font=("Arial",10)).pack()


        tk.Button(ventana, text="Volver", command=ventana_menu_administrador, bg="lightcoral").pack()

    mostrar_ventana_principal()
    ventana.mainloop()

if __name__ == "__main__":
    ventana_principal()

