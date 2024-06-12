
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

def buscar_pelicula(nombre):
    if nombre in peliculas:
        print(f'La película "{nombre}" está en la lista.')
    else:
        print(f'La película "{nombre}" no está en la lista.')

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

def salir():
    global continuar
    continuar = False

continuar = True

while continuar:
    limpiar_pantalla()
    print("\n\t..::: SISTEMA DE PELÍCULAS :::...")
    print("1. Agregar Película")
    print("2. Remover Película")
    print("3. Buscar Película")
    print("4. Consultar Películas")
    print("5. Vaciar Lista de Películas")
    print("6. Salir")
    opcion = input("\n\tElige una opción: ")

    if opcion == "1":
        nombre = input("Ingrese el nombre de la película a agregar: ")
        agregar_pelicula(nombre)
        pausar()
    elif opcion == "2":
        nombre = input("Ingrese el nombre de la película a remover: ")
        remover_pelicula(nombre)
        pausar()
    elif opcion == "3":
        nombre = input("Ingrese el nombre de la película a buscar: ")
        buscar_pelicula(nombre)
        pausar()
    elif opcion == "4":
        consultar_peliculas()
        pausar()
    elif opcion == "5":
        peliculas.clear()
        print("Lista de películas vaciada.")
        pausar()
    elif opcion == "6":
        salir()
    else:
        print("Opción no válida. Por favor, selecciona una opción válida.")
        pausar()