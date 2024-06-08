import os
from otras_funciones import *

# def solicitarNumeros():
#   global n1,n2  
#   n1=int(input("Numero #1: "))
#   n2=int(input("Numero #2: "))
  

# def operacionAritmetica(num1,num2,opcion):  
#     if opcion=="1" or opcion=="+" or opcion=="SUMA":
#       return f"{n1}+{n2}={n1+n2}"
#     elif opcion=="2" or opcion=="-" or opcion=="RESTA":
#      return f"{n1}-{n2}={n1-n2}"
#     elif opcion=="3" or opcion=="*" or opcion=="MULTIPLICACION":
#      return f"{n1}*{n2}={n1*n2}"
#     elif opcion=="4" or opcion=="/" or opcion=="DIVISION":
#      return f"{n1}/{n2}={n1/n2}"  
    
# def esperarTecla():
#   print("Oprima cualquier tecla para continuar ...")
#   input()

# opcion=True 
   
# while opcion:
#  os.system("clear")
#  print("\n\t..::: CALCULADORA BÁSICA :::... \n 1.- Suma \n 2.- Resta \n 3.- Multiplicacion \n 4.- División \n 5.- SALIR ")
#  opcion=input("\t Elige una opción: ").upper()
 
#  if opcion!="5":
#   n1,n2=solicitarNumeros()
#   print(operacionAritmetica(n1,n2,opcion))
#   esperarTecla()
#  else:  
#      opcion=False    
#      print("Terminaste la ejecucion del SW")


    #  SISTEMA PELICULAS
    peliculas = []

def agregar_pelicula(nombre):
    peliculas.append(nombre)
    print(f'Película "{nombre}" agregada correctamente.')

def remover_pelicula(nombre):
    if nombre in peliculas:
        peliculas.remove(nombre)
        print(f'Película "{nombre}" removida correctamente.')
    else:
        print(f'Película "{nombre}" no encontrada.')

def consultar_peliculas():
    if peliculas:
        print("Listado de películas:")
        for idx, pelicula in enumerate(peliculas, start=1):
            print(f'{idx}. {pelicula}')
    else:
        print("No hay películas en la lista.")

def actualizar_pelicula(viejo_nombre, nuevo_nombre):
    if viejo_nombre in peliculas:
        index = peliculas.index(viejo_nombre)
        peliculas[index] = nuevo_nombre
        print(f'Película "{viejo_nombre}" actualizada a "{nuevo_nombre}".')
    else:
        print(f'Película "{viejo_nombre}" no encontrada.')

def limpiar_pantalla():
    import os
    import platform
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def pausar():
    input("Presiona una tecla para continuar...")
