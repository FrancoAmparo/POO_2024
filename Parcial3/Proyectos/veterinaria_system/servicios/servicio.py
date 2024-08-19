from conexionBD import conectar

class Servicio:
    def __init__(self, nombre, descripcion, precio):
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio

    def registrar(self):
        try:
            conexion = conectar()
            cursor = conexion.cursor()
            cursor.execute(
                "INSERT INTO servicios (nombre, descripcion, precio) VALUES (%s, %s, %s)",
                (self.nombre, self.descripcion, self.precio)
            )
            conexion.commit()
            return True
        except Exception as e:
            print(f"Error al registrar servicio: {e}")
            if conexion:
                conexion.rollback()
            return False
        finally:
            if conexion:
                conexion.close()

    @staticmethod
    def actualizar(id_servicio, nombre, descripcion, precio):
        try:
            conexion = conectar()
            cursor = conexion.cursor()
            cursor.execute(
                "UPDATE servicios SET nombre=%s, descripcion=%s, precio=%s WHERE id_servicio=%s",
                (nombre, descripcion, precio, id_servicio)
            )
            conexion.commit()
            return True
        except Exception as e:
            print(f"Error al actualizar servicio: {e}")
            if conexion:
                conexion.rollback()
            return False
        finally:
            if conexion:
                conexion.close()

    @staticmethod
    def eliminar(id_servicio):
        try:
            conexion = conectar()
            cursor = conexion.cursor()
            cursor.execute("DELETE FROM servicios WHERE id_servicio=%s", (id_servicio,))
            conexion.commit()
            return True
        except Exception as e:
            print(f"Error al eliminar servicio: {e}")
            if conexion:
                conexion.rollback()
            return False
        finally:
            if conexion:
                conexion.close()

    @staticmethod
    def buscar(id_servicio):
        try:
            conexion = conectar()
            cursor = conexion.cursor()
            cursor.execute("SELECT * FROM servicios WHERE id_servicio=%s", (id_servicio,))
            return cursor.fetchone()
        except Exception as e:
            print(f"Error al buscar servicio: {e}")
            return None
        finally:
            if conexion:
                conexion.close()
