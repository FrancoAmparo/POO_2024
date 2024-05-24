



#Ejemplo 2 crear un programa que imprima los numeros del 1 al 5, los sume e implrmima la suma al final

suma=0
contador=1
while contador<=5:
    print(contador)
    suma+=contador
    contador+=1
    print(f"la suma es: {suma}")

        #Ejemplo 3 crear un programa que solicite un numero y apartir de este numero genere e imprima la tabla de multiplicar correspondiente

numero=int (input("ingrese un numero: "))

multi=0
i=1
while i<=10:
     multi=numero*i
     i+=1
     print(f"{numero} X {i} = {multi}")
     i+=1
print()