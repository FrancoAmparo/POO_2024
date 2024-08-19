from conexionBD import conectar_bd

def agregar_administrador(nombre, password, correo):
    conn = conectar_bd()
    cursor = conn.cursor()

    cursor.execute("INSERT INTO trabajadores (nombre, edad) VALUES (%s, %s)", 
                   (nombre, 0))  
    trabajador_id = cursor.lastrowid

    cursor.execute("INSERT INTO empleados (trabajador_id, jornada, prima_dominical) VALUES (%s, %s, %s)", 
                   (trabajador_id, 'no aplica', 0)) 
    empleado_id = cursor.lastrowid

    cursor.execute("INSERT INTO administradores (empleado_id, password, correo) VALUES (%s, %s, %s)", 
                   (empleado_id, password, correo))
    conn.commit()
    cursor.execute("SELECT LAST_INSERT_ID()")
    admin_id = cursor.fetchone()[0]
    conn.close()
    
    return admin_id

def iniciar_sesion(correo, password):
    conn = conectar_bd()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT a.*
        FROM administradores a
        JOIN empleados e ON a.empleado_id = e.id
        JOIN trabajadores t ON e.trabajador_id = t.id
        WHERE a.correo = %s AND a.password = %s
    """, (correo, password))
    admin = cursor.fetchone()
    conn.close()
    return admin
