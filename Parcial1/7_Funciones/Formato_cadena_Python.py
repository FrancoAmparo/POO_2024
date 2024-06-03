#1_CUERDAS EN PYTHON 
cadena_simple='Hola, Mundo!'
cadena_doble="Hola, Mundo!"
print(cadena_doble)
print(cadena_simple)
print()
#CADENA MULTILINEA
cadena_mulltilinea='''Esta es una cadena de varias lineas'''
print(cadena_mulltilinea)
print()
#2_MARCADORES DE POSICION Y MODIFICADORES
nombre="Juan"
edad=25
texto="Me llamo {} y tengo {} años.".format(nombre, edad) 
print(texto)
print()
#3_REALIZAR OPERACIONES EN F-STRINGS 
a=25
b=10
print(f"la suma de {a} y {b} es {a + b}")
print()
#4_EJECUTAR FUNCIONES EN F-STRINGS 
def mayuscula(texto):
    return texto.upper()

print(f'Texto en mayusculas: {mayuscula("hola")}')
print()
#5_FORMATO DE CADENA
   #Metodo '.format()'

nombree="Manuel"
edaad=22
texto="Me llamo {0} y tengo {1} años. {0} es un buen nombre".format(nombree, edaad)
print()
#6_VALORES MULTIPLES
nombres=["Ana", "Luis", "Marta"]
print("Los nombres son: {}, {} y {}".format(nombres[0], nombres[1], nombres[2])) 
print()
#7_INDICES CON NOMBRE
persona={"noombre": "Mario", "eedad":35}
texto="Me llamo {noombre} y tengo {eedad}".format(**persona)

