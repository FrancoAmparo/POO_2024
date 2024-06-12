#1.- 
# Hacer un programa que tenga una lista de 8 numeros enteros y realice lo siguiente: 

#  a.- Recorrer la lista y mostrarla
#  b.- hacer una funcion que recorra la lista de numeros y devuelva un string
#  c.- ordenarla y mostrarla
#  d.- mostrar su longitud
#  e.- buscar algun elemento que el usuario pida por teclado

numeros = [8, 3, 1, 7, 2, 6, 4, 5]


print("a.- RECORRER LA LISTA:")
for numero in numeros:
    print(numero)

def lista_a_string(lista):
    try:
        resultado = ""
        for i in range(len(lista)):
            resultado += str(lista[i])
            if i < len(lista) - 1:
                resultado += ", "
        return resultado
    except:
        return "Error al convertir la lista a string."


print("\nb.- CONVERTIR LA LISTA A STRING:")
print(lista_a_string(numeros))


print("\nc.- ORDENAR LA LISTA Y MOSTRARLA :")
try:
    numeros_ordenados = numeros[:]
    for i in range(len(numeros_ordenados)):
        for j in range(i + 1, len(numeros_ordenados)):
            if numeros_ordenados[i] > numeros_ordenados[j]:
                numeros_ordenados[i], numeros_ordenados[j] = numeros_ordenados[j], numeros_ordenados[i]
    print(numeros_ordenados)
except:
    print("Error al ordenar la lista.")


print("\nd.- MOSTRAR LA LONGITUD DE LA LISTA:")
try: 
    print(len(numeros))
except:
    print("Error al obtener la longitud de la lista.")


print("\ne.- BUSCAR UN ELEMENTO EN LA LISTA")
try:
    elemento_a_buscar = int(input("Introduce el número a buscar: "))
    encontrado = False
    for numero in numeros:
        if numero == elemento_a_buscar:
            encontrado = True
            break
    if encontrado:
        print(f"El número {elemento_a_buscar} se encuentra en la lista.")
    else:
        print(f"El número {elemento_a_buscar} NO se encuentra en la lista.")
except ValueError:
    print("introduce un número entero válido.")
except:
    print("Error al buscar el numero.")
    print()