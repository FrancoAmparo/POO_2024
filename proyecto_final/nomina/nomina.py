from conexionBD import conectar_bd
from empleados.empleado import Empleado

def registrar_empleado(nombre, edad, horas_trabajadas, sueldo_dia, prima_dominical, tipo_jornada, dias_trabajados, horas_extra, descanso_semanal):
    conn = conectar_bd()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO trabajadores (nombre, edad) VALUES (%s, %s)", 
                   (nombre, edad))
    trabajador_id = cursor.lastrowid
    empleado = Empleado(trabajador_id, nombre, edad, horas_trabajadas, sueldo_dia, prima_dominical, tipo_jornada, dias_trabajados, horas_extra, descanso_semanal)

    cursor.execute("INSERT INTO empleados (trabajador_id, jornada, prima_dominical) VALUES (%s, %s, %s)", 
                   (empleado.trabajador_id, empleado.tipo_jornada, empleado.prima_dominical))
    empleado_id = cursor.lastrowid
    cursor.execute("INSERT INTO nomina (empleado_id, salario_base) VALUES (%s, %s)", 
                   (empleado_id, empleado.salario_base))

    conn.commit()
    conn.close()
    return trabajador_id

def ver_salarios():
    conn = conectar_bd()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT t.nombre, n.salario_base, COALESCE(b.monto, 0) AS bono, 
               (n.salario_base + COALESCE(b.monto, 0)) AS salario_total, n.fecha_registro
        FROM nomina n
        JOIN empleados e ON n.empleado_id = e.id
        JOIN trabajadores t ON e.trabajador_id = t.id
        LEFT JOIN bonos b ON n.empleado_id = b.empleado_id
        ORDER BY n.fecha_registro DESC
    """)
    resultados = cursor.fetchall()
    conn.close()
    return resultados
