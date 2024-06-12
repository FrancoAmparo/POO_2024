# #2.- Escribir un programa  que añada valores a una lista mientras que su longitud 
#  sea menor a 120, y luego mostrar la lista: Usar un while y for
lista = []

try:
    while len(lista) < 121:
        lista.append(len(lista))

except:
    print("Ocurrió un error al añadir valores a la lista: ")

else:
    for valor in lista:
        print(valor)

finally:
    print("Proceso completado.")