from conexionBD import conectar

class Cliente:
    def __init__(self, id_persona):
        self.id_persona = id_persona

    def registrar(self):
        try:
            conexion = conectar()
            cursor = conexion.cursor()
            cursor.execute(
                "INSERT INTO clientes (id_persona) VALUES (%s)",
                (self.id_persona,)
            )
            conexion.commit()
            return True
        except Exception as e:
            print(f"Error al registrar cliente: {e}")
            if conexion:
                conexion.rollback()
            return False
        finally:
            if conexion:
                conexion.close()

    @staticmethod
    def eliminar(id_cliente):
        try:
            conexion = conectar()
            cursor = conexion.cursor()
            cursor.execute("DELETE FROM clientes WHERE id_cliente=%s", (id_cliente,))
            conexion.commit()
            return True
        except Exception as e:
            print(f"Error al eliminar cliente: {e}")
            if conexion:
                conexion.rollback()
            return False
        finally:
            if conexion:
                conexion.close()

    @staticmethod
    def buscar(id_cliente): 
        try:
            conexion = conectar()
            cursor = conexion.cursor()
            cursor.execute("SELECT * FROM clientes WHERE id_cliente=%s", (id_cliente,))
            return cursor.fetchone()
        except Exception as e:
            print(f"Error al buscar cliente: {e}")
            return None
        finally:
            if conexion:
                conexion.close()