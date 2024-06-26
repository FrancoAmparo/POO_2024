"""
list (Array)
son colecciones o conjunto de datos/valores bajo un mismo nombre, para acceder a los
 valores se hace con un indice numerico

 Nota: sus valores si son modificables

 La lista es una coleccion ordenada y modificable 
 Permite miembros duplicados

 """
 #EJEMPLO 1
 #Crear una lista de numeros e imprimir el contenido

# numeros[23,34]
# print(numeros)

# #Recorrer la lista con un ciclo for
# for i in numeros:
#     print(i)

# #Recorrer la lista con un ciclo while
# i=0


# while i<=len(numeros)-1:
#     print(numeros[i])
#     i+=1


#Ejemplo2
#crear una lista de palabras, posteriormente buscar la coincidencia de una palabra
# palabra = ["hola","utd", "como", "estas", "ok", "naranja"]
# palabra_buscar = input("inserta palabra a buscar: ")

# if palabra_buscar in palabra:
#     for i, p in enumerate(palabra):
#         if p == palabra_buscar:
#             print(f"Encontré la palabra en la posición {i+1}")
# else:
#     print("No encontré la palabra en la lista")


#While
#while
# palabras = ["hola", "utd", "estas", "nada", "ok", "naranja"]
# buscar = input("inserta palabra a buscar: ")
# i = 0
# encontrado = False
# while i < len(palabras):
#     if palabras[i] == buscar:
#         encontrado = True
#         break
#     i +=2
# if encontrado:
#     print(f"La palabra '{buscar}' se encontró en la lista en la posición {i+1}.")
# else:
#     print(f"La palabra '{buscar}' no se encontró en la lista.")


#4_Crear una lista multilinea (matriz ) para agregar los nombres y numeros telefonicos 
# agenda=
# ("carlos", 6181234567,
# leo=, 6671234573,
# "sebastia", 6181231234,
# "pedro", 618113334455
# )
# print(agenda)
# for i in agenda:
# print(f(agenda.index(i)+1),-(i))


#5_Crear un programa que permita gestionar (administrar) pelicula, coloca un menu de opciones
#para agregar, remover, consultar peliculas
#NOTAS:
#1_utiliza funciones y mandar llamar desde otro archivo
#2_utilizar listas para almacenar los nombres de peliculas

from calculadora_basica import agregar_pelicula, remover_pelicula, consultar_peliculas, actualizar_pelicula, limpiar_pantalla, pausar

def menu():
    while True:
        limpiar_pantalla()
        print("Gestión de Películas")
        print("1. Agregar Película")
        print("2. Remover Película")
        print("3. Consultar Películas")
        print("4. Actualizar Película")
        print("5. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            limpiar_pantalla()
            nombre = input("Ingrese el nombre de la película: ")
            agregar_pelicula(nombre)
            pausar()
        elif opcion == '2':
            limpiar_pantalla()
            nombre = input("Ingrese el nombre de la película a remover: ")
            remover_pelicula(nombre)
            pausar()
        elif opcion == '3':
            limpiar_pantalla()
            consultar_peliculas()
            pausar()
        elif opcion == '4':
            limpiar_pantalla()
            viejo_nombre = input("Ingrese el nombre de la película a actualizar: ")
            nuevo_nombre = input("Ingrese el nuevo nombre de la película: ")
            actualizar_pelicula(viejo_nombre, nuevo_nombre)
            pausar()
        elif opcion == '5':
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida.")
            pausar()

if __name__ == "__main__":
    menu()









# #Ejemplo 3 agregar y elimiinar elementos de una lista
# #os.system("clear")

# numeros =[23,34,23]
# print(numeros)

# #Agregar un elemento
# numeros.append(100)
# print(numeros)
# numeros.insert(3,200)
# print(numeros)

# #Eliminar un elemento 
# numeros.remove(100) #Indicar el elemto a borrar 
# print(numeros)
# numeros.pop(2)#Indicar la posicion de el elemnto a borrar 
# print(numeros)
print()






