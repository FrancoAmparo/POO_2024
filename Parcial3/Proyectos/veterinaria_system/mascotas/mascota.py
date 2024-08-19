from conexionBD import conectar

class Mascota:
    def __init__(self, nombre, tipo, raza, edad, id_cliente):
        self.nombre = nombre
        self.tipo = tipo
        self.raza = raza
        self.edad = edad
        self.id_cliente = id_cliente

    def registrar(self):
        try:
            conexion = conectar()
            cursor = conexion.cursor()
            cursor.execute(
                "INSERT INTO mascotas (nombre, tipo, raza, edad, id_cliente) VALUES (%s, %s, %s, %s, %s)",
                (self.nombre, self.tipo, self.raza, self.edad, self.id_cliente)
            )
            conexion.commit()
            return True
        except Exception as e:
            print(f"Error al registrar la mascota: {e}")
            if conexion:
                conexion.rollback()
            return False
        finally:
            if conexion:
                conexion.close()

    @staticmethod
    def eliminar(id_mascota):
        try:
            conexion = conectar()
            cursor = conexion.cursor()
            cursor.execute("DELETE FROM mascotas WHERE id_mascota=%s", (id_mascota,))
            conexion.commit()
            return True
        except Exception as e:
            print(f"Error al eliminar mascota: {e}")
            if conexion:
                conexion.rollback()
            return False
        finally:
            if conexion:
                conexion.close()

    @staticmethod
    def buscar(id_mascota):
        try:
            conexion = conectar()
            cursor = conexion.cursor()
            cursor.execute("SELECT * FROM mascotas WHERE id_mascota=%s", (id_mascota,))
            return cursor.fetchone()
        except Exception as e:
            print(f"Error al buscar mascota: {e}")
            return None
        finally:
            if conexion:
                conexion.close()
