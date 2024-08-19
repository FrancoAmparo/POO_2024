from conexionBD import conectar

class Consulta:
    def __init__(self, id_mascota, id_empleado, fecha, diagnostico, tratamiento):
        self.id_mascota = id_mascota
        self.id_empleado = id_empleado
        self.fecha = fecha
        self.diagnostico = diagnostico
        self.tratamiento = tratamiento

    def registrar(self):
        try:
            conexion = conectar()
            cursor = conexion.cursor()
            cursor.execute(
                "INSERT INTO consultas (id_mascota, id_empleado, fecha, diagnostico, tratamiento) VALUES (%s, %s, %s, %s, %s)",
                (self.id_mascota, self.id_empleado, self.fecha, self.diagnostico, self.tratamiento)
            )
            conexion.commit()
            return True
        except Exception as e:
            print(f"Error al registrar la consulta: {e}")
            if conexion:
                conexion.rollback()
            return False
        finally:
            if conexion:
                conexion.close()

    @staticmethod
    def eliminar(id_consulta):
        try:
            conexion = conectar()
            cursor = conexion.cursor()
            cursor.execute("DELETE FROM consultas WHERE id_consulta=%s", (id_consulta,))
            conexion.commit()
            return True
        except Exception as e:
            print(f"Error al eliminar consulta: {e}")
            if conexion:
                conexion.rollback()
            return False
        finally:
            if conexion:
                conexion.close()

    @staticmethod
    def buscar(id_consulta):
        try:
            conexion = conectar()
            cursor = conexion.cursor()
            cursor.execute("SELECT * FROM consultas WHERE id_consulta=%s", (id_consulta,))
            return cursor.fetchone()
        except Exception as e:
            print(f"Error al buscar consulta: {e}")
            return None
        finally:
            if conexion:
                conexion.close()