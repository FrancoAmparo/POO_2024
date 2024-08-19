from conexionBD import conectar

class Vacuna:
    def __init__(self, nombre, descripcion):
        self.nombre = nombre
        self.descripcion = descripcion

    def registrar(self):
        try:
            conexion = conectar()
            cursor = conexion.cursor()
            cursor.execute(
                "INSERT INTO vacunas (nombre, descripcion) VALUES (%s, %s)",
                (self.nombre, self.descripcion)
            )
            conexion.commit()
            return True
        except Exception as e:
            print(f"Error al registrar vacuna: {e}")
            if conexion:
                conexion.rollback()
            return False
        finally:
            if conexion:
                conexion.close()

    @staticmethod
    def eliminar(id_vacuna):
        try:
            conexion = conectar()
            cursor = conexion.cursor()
            cursor.execute("DELETE FROM vacunas WHERE id_vacuna=%s", (id_vacuna,))
            conexion.commit()
            return True
        except Exception as e:
            print(f"Error al eliminar vacuna: {e}")
            if conexion:
                conexion.rollback()
            return False
        finally:
            if conexion:
                conexion.close()

    @staticmethod
    def buscar(id_vacuna):
        try:
            conexion = conectar()
            cursor = conexion.cursor()
            cursor.execute("SELECT * FROM vacunas WHERE id_vacuna=%s", (id_vacuna,))
            return cursor.fetchone()
        except Exception as e:
            print(f"Error al buscar vacuna: {e}")
            return None
        finally:
            if conexion:
                conexion.close()
