paises=["Mexico", "USA", "Brasil", "Japon"]
numeros=[23, 100, 3.1416, 0.100]
varios=["Hola",True, 100, 10,22]

#Ordenar la lista

print(paises)
paises.sort()
print(paises)

#Agregar elementos 
print(numeros)
numeros.insert(len(numeros), 100)
print(numeros)
numeros.append(100)

#Eliminar elementos
print(numeros)
numeros.pop(2)
print(numeros)
numeros.remove(100)

#Buscar dentro de una lista un dato

encontrar="Brasil" in paises
print(encontrar)

#Dar la vuelta
print(varios)
varios.reverse()
print(varios)

#Unir listas
print(paises)
paises.extend(numeros)
print(paises)

#Vaciar una lista
print(varios)
varios.clear()
print(varios)