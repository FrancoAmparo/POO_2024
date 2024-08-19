from conexionBD import conectar

class Persona:
    def __init__(self, nombre, apellido, direccion, telefono, email):
        self.nombre = nombre
        self.apellido = apellido
        self.direccion = direccion
        self.telefono = telefono
        self.email = email

    def registrar(self):
        try:
            conexion = conectar()
            cursor = conexion.cursor()
            cursor.execute(
                "INSERT INTO personas (nombre, apellido, direccion, telefono, email) VALUES (%s, %s, %s, %s, %s)",
                (self.nombre, self.apellido, self.direccion, self.telefono, self.email)
            )
            conexion.commit()
            return True
        except Exception as e:
            print(f"Error al registrar persona: {e}")
            if conexion:
                conexion.rollback()
            return False
        finally:
            if conexion:
                conexion.close()

    def actualizar(self, id_persona):
        try:
            conexion = conectar()
            cursor = conexion.cursor()
            cursor.execute(
                "UPDATE personas SET nombre=%s, apellido=%s, direccion=%s, telefono=%s, email=%s WHERE id_persona=%s",
                (self.nombre, self.apellido, self.direccion, self.telefono, self.email, id_persona)
            )
            conexion.commit()
            return True
        except Exception as e:
            print(f"Error al actualizar persona: {e}")
            if conexion:
                conexion.rollback()
            return False
        finally:
            if conexion:
                conexion.close()

    @staticmethod
    def eliminar(id_persona):
        try:
            conexion = conectar()
            cursor = conexion.cursor()
            cursor.execute("DELETE FROM personas WHERE id_persona=%s", (id_persona,))
            conexion.commit()
            return True
        except Exception as e:
            print(f"Error al eliminar persona: {e}")
            if conexion:
                conexion.rollback()
            return False
        finally:
            if conexion:
                conexion.close()

    @staticmethod
    def buscar(id_persona):
        try:
            conexion = conectar()
            cursor = conexion.cursor()
            cursor.execute("SELECT * FROM personas WHERE id_persona=%s", (id_persona,))
            return cursor.fetchone()
        except Exception as e:
            print(f"Error al buscar persona: {e}")
            return None
        finally:
            if conexion:
                conexion.close()
