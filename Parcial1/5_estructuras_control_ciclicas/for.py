#El for es una estructura de control repetitiva o ciclica que funciona con iteraciones x veces de acuerdo a los valures numericos enterosque contenga 

#sintaxis:

#for variable in elemento_iterable(list, range, etc):
#Ejemplo 1 crear un programa que imprima 5 veces el caracter @


for contador in range (1,6):
     print("@")



     #Ejemplo 2 crear un programa que imprima los numeros del 1 al 5, los sume e implrmima la suma al final

suma=0
for contador in range (1,6):
    print(contador)
    suma+=contador
    print(f"la suma es: {suma}")


    #Ejemplo 3 crear un programa que solicite ubn numero y apartir de este numero genere e imprima la tabla de multiplicar correspondiente

numero=int (input("ingrese un numero: "))

multi=0
for i in range(1,11):
     multi=numero*i
     print(f"{numero} X {i} = {multi}")

print()