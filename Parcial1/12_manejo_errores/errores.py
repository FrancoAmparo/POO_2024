#Los errores de ejcucion en un lenguaje de programacion se presenta cuando existe una anomalia o error
#dentro de la ejecucion del codigo lo cual provoca que se detenga la ejecucion del sw, con el control
# y manejo de excepciones
#sera posible minimisar o evetar la interrupcion del programa debido a una excepcion

#Ejemplo 1 cuando una variable no se genera 

# try:
#      nombre=input("Introduce el nombre completo de la persona: ")
#      if len(nombre)>0:
#         nombre_usuario="el nombre completo del usuario es: "+nombre

#         print(nombre_usuario)

# except:
#         print("Es necesario introducir un nombre de usuario...verifica por favor")


#Ejemplo 2 Cuando se solicita un numero y se ingresa otra cosa



# try:
#     numero=int(input("Ingrese un numero entero: "))

#     if numero>0:
#           print("Soy un numero entero positivo")
#     elif numero==0:
#          print("Soy un numero neutro")
#     else:
#          print("Soy un numero negativo")
# except ValueError:
#      print("Introduce un valor numerico entero")
     

#Ejemplo 3 Generan multiples excepciones

try:
     numero=int(input("Introduce un numero: "))

     print("El cuadrado del numero es: "+str(numero*numero))
except ValueError:
     print("Introduce un valor numerico entero")
except TypeError:
     print("Se debe convertir el numero a entero")
else:
     print("No se presentaron errores de ejecucion")
finally:
     print("Termine la ejecucion")