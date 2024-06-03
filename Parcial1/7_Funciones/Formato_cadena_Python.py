# 1_CUERDAS EN PYTHON 

cadena_simple='Hola, Mundo!'
cadena_doble="Hola, Mundo!"
print(cadena_simple)
print(cadena_doble)

#2_CADENA MULTILINEA

cadena_multilinea='''Esta es una cadena de varias lineas'''
print(cadena_multilinea)

#3_MARCADORES DE POSICION Y MODIFICADORES

nombre="Juan"
edad=25
texto="Me llamo {} y tengo {} años.".format(nombre, edad)
print(texto)

#MODIFICADORES
numero=3.14159
print("El numero es {:.2f}".format(numero))

#REALIZAR OPERACIONES EN F-STRINGS

        #OPERACIONES
a=5
b=10
print(f"la suma de {a} y {b} es {a + b}")

     #OTRO EJEMPLO
name= Emilio
edadd=22
print(f"Me llamo {name} y el proximo año tendre {edadd + 1} años")

#EJECUTAR FUNCIONES EN F-STRINGS 

def mayuscula(texto):
    return texto.upper()

print(f"Texto en mayusculas: {mayuscula("hola")}")

#FORMATO DE CADENA
#Metodo .format()

nombree=Manuel
cant_años=31
texto="Me llamo {0} y tengo {1} años. {0} es un buen nombre.".format(nombree, cant_años)
print(texto)

#VALORES MULTIPLES

nombres=["Ana", "luis", "Marta"]
print("Los nombres son: {}, {}, y {}".format(nombres[0], nombres[1], nombres[2]))

