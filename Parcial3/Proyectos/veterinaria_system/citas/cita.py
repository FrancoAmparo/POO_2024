from conexionBD import conectar

class Cita:
    def __init__(self, fecha, hora, id_cliente, id_mascota, id_servicio):
        self.fecha = fecha
        self.hora = hora
        self.id_cliente = id_cliente
        self.id_mascota = id_mascota
        self.id_servicio = id_servicio

    def registrar(self):
        conexion = None
        try:
            conexion = conectar()
            cursor = conexion.cursor()
            cursor.execute(
                "INSERT INTO citas (fecha, hora, id_cliente, id_mascota, id_servicio) VALUES (%s, %s, %s, %s, %s)",
                (self.fecha, self.hora, self.id_cliente, self.id_mascota, self.id_servicio)
            )
            conexion.commit()
            return True
        except Exception as e:
            print(f"Error al registrar la cita: {e}")
            if conexion:
                conexion.rollback()
            return False
        finally:
            if conexion:
                conexion.close()
