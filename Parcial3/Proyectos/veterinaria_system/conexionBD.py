import mysql.connector
import sqlite3

def conectar():
    try:
        conexion = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='bd_veterinaria'
        )
        return conexion
    except mysql.connector.Error as e:
        print(f"Error al conectar con la base de datos: {e}")
        return None
