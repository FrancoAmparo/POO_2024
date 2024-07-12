from conexionBD import *
try:
     micursor=conexion.cursor()
     sql="delete from clientes where id=1"

     micursor.execute(sql)
     conexion.commit()

except:
          print(f"Ocurrio un problema con el servidor...porfavor intentalo mas tarde...")
else:
          print("Registro Eliminado Correctamente")