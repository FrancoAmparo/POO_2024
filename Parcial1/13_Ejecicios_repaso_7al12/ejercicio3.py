
# Crear un programa para comprobar si una lista esta vacia y si esta vacia llenarla con 
#  palabras o frases hasta que el usuario asi lo crea conveniente, posteriormente imprimir 
#  el contenido de la lista en mayusculas

lista = []

try:
    if not lista:
        print("La lista está vacía. Vamos a llenarla.")
        
        while True:
            entrada = input("Introduce una palabra o frase (o 'salir' para terminar): ")
            
            if entrada== 'salir':
                break
    
            lista.append(entrada)

except:
    print("Ocurrió un error: ")

finally:
    if lista:
        print("Contenido de la lista:")
        for it in lista:
            print(it.upper())
    else:
        print("La lista sigue vacía.")
