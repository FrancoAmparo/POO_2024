from conexionBD import conectar_bd

def asignar_bono(empleado_id, monto):
    conn = conectar_bd()
    cursor = conn.cursor()
    
    cursor.execute("SELECT id FROM empleados WHERE id = %s", (empleado_id,))
    resultado = cursor.fetchone()
    
    if resultado is None:
        print(f"Error: El empleado con ID {empleado_id} no existe.")
    else:

        cursor.execute("INSERT INTO bonos (empleado_id, monto) VALUES (%s, %s)", (empleado_id, monto))
        conn.commit()
        print("Bono asignado con éxito.")
    
    conn.close()