# Crear una lista y un diccionario con el contenido de esta tabla: 

#   ACCION              TERROR        DEPORTES
#   MAXIMA VELOCIDAD    LA MONJA       ESPN
#   ARMA MORTAL 4       EL CONJURO     MAS DEPORTE
#   RAPIDO Y FURIOSO I  LA MALDICION   ACCION


#   imprimir la información



def crear_lista_y_diccionario():
    try:

        tabla_lista = [
            ["ACCION", "TERROR", "DEPORTES"],
            ["MAXIMA VELOCIDAD", "LA MONJA", "ESPN"],
            ["ARMA MORTAL 4", "EL CONJURO", "MAS DEPORTE"],
            ["RAPIDO Y FURIOSO I", "LA MALDICION", "ACCION"]
        ]


        tabla_diccionario = {
            "ACCION": ["MAXIMA VELOCIDAD", "ARMA MORTAL 4", "RAPIDO Y FURIOSO I"],
            "TERROR": ["LA MONJA", "EL CONJURO", "LA MALDICION"],
            "DEPORTES": ["ESPN", "MAS DEPORTE", "ACCION"]
        }

        return tabla_lista, tabla_diccionario
    except:
        print("Ocurrió un error al crear la lista y el diccionario: ")
        return [], {}

def imprimir_informacion(tabla_lista, tabla_diccionario):
    try:
        print("Contenido de la lista:")
        for fila in tabla_lista:
            print(*fila)

        print("\nContenido del diccionario:")
        for clave in tabla_diccionario:
            print(clave + ":", end=" ")
            print(*tabla_diccionario[clave])
    except:
        print("Ocurrió un error al imprimir la información: ")


lista, diccionario = crear_lista_y_diccionario()

if lista and diccionario:
    imprimir_informacion(lista, diccionario)
    print()