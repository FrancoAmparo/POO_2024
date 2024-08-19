from conexionBD import conectar

class Empleado:
    def __init__(self, id_persona, puesto):
        self.id_persona = id_persona
        self.puesto = puesto

    def registrar(self):
        try:
            conexion = conectar()
            cursor = conexion.cursor()
            cursor.execute(
                "INSERT INTO empleados (id_persona, puesto) VALUES (%s, %s)",
                (self.id_persona, self.puesto)
            )
            conexion.commit()
            return True
        except Exception as e:
            print(f"Error al registrar empleado: {e}")
            if conexion:
                conexion.rollback()
            return False
        finally:
            if conexion:
                conexion.close()

    @staticmethod
    def eliminar(id_empleado):
        try:
            conexion = conectar()
            cursor = conexion.cursor()
            cursor.execute("DELETE FROM empleados WHERE id_empleado=%s", (id_empleado,))
            conexion.commit()
            return True
        except Exception as e:
            print(f"Error al eliminar empleado: {e}")
            if conexion:
                conexion.rollback()
            return False
        finally:
            if conexion:
                conexion.close()

    @staticmethod
    def buscar(id_empleado):
        try:
            conexion = conectar()
            cursor = conexion.cursor()
            cursor.execute("SELECT * FROM empleados WHERE id_empleado=%s", (id_empleado,))
            return cursor.fetchone()
        except Exception as e:
            print(f"Error al buscar empleado: {e}")
            return None
        finally:
            if conexion:
                conexion.close()
