from conexionBD import conectar

class Veterinaria:
    @staticmethod
    def obtener_informacion():
        try:
            conexion = conectar()
            if conexion is None:
                raise Exception("No se pudo establecer la conexión con la base de datos.")
            
            cursor = conexion.cursor()

            cursor.execute("SELECT COUNT(*) FROM personas")
            total_personas = cursor.fetchone()[0]

            cursor.execute("SELECT COUNT(*) FROM clientes")
            total_clientes = cursor.fetchone()[0]

            cursor.execute("SELECT COUNT(*) FROM empleados")
            total_empleados = cursor.fetchone()[0]

            cursor.execute("SELECT COUNT(*) FROM mascotas")
            total_mascotas = cursor.fetchone()[0]

            cursor.execute("SELECT COUNT(*) FROM vacunas")
            total_vacunas = cursor.fetchone()[0]

            cursor.execute("SELECT COUNT(*) FROM consultas")
            total_consultas = cursor.fetchone()[0]

            return {
                'total_personas': total_personas,
                'total_clientes': total_clientes,
                'total_empleados': total_empleados,
                'total_mascotas': total_mascotas,
                'total_vacunas': total_vacunas,
                'total_consultas': total_consultas,
            }
        except Exception as e:
            print(f"Error al obtener información general: {e}")
            return None
        finally:
            if conexion:
                conexion.close()

