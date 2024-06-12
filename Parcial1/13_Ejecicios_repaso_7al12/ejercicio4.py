#  Crear un script que tenga 4 variables, una lista, una cadena, un entero y un logico,  
#   y que imprima un mensaje de acuerdo al tipo de dato de cada variable. Usar funciones

def comprobar_tipo(variable):
    try:
        tipo = type(variable).__name__
        if tipo == 'list':
            print("La variable es una lista.")
        elif tipo == 'str':
            print("La variable es una cadena.")
        elif tipo == 'int':
            print("La variable es un entero.")
        elif tipo == 'bool':
            print("La variable es un booleano.")
        else:
            print("La variable es de un tipo desconocido.")
    except:
        print("Ocurrió un error al comprobar el tipo: ")

lista = [1, 2, 3]
cadena = "Hola, mundo"
entero = 42
logico = True

comprobar_tipo(lista)
comprobar_tipo(cadena)
comprobar_tipo(entero)
comprobar_tipo(logico)
print()