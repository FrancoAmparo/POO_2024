

from conexionBD import conectar_bd

def enviar_notificacion(empleado_id, mensaje, admin_id):
    conn = conectar_bd()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO notificaciones (mensaje, empleado_id, admin_id) VALUES (%s, %s, %s)", 
                   (mensaje, empleado_id, admin_id))
    conn.commit()
    conn.close()

def ver_notificaciones():
    conn = conectar_bd()
    cursor = conn.cursor()
    
    cursor.execute("""
        SELECT n.mensaje, n.fecha_envio, t.nombre AS nombre_empleado, a.correo AS correo_admin
        FROM notificaciones n
        JOIN empleados e ON n.empleado_id = e.id
        JOIN trabajadores t ON e.trabajador_id = t.id
        JOIN administradores a ON n.admin_id = a.id
        ORDER BY n.fecha_envio DESC
    """)
    notificaciones = cursor.fetchall()
    conn.close()
    return notificaciones