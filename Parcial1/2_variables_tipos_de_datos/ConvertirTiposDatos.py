#Convertir los tipos de datos

#NOTA: Solo es posible en una concatenacion concatenar entre tipos de datos iguales

texto="soy una cadena"
numero=23


print(texto+" y soy una cadena2")
print(numero+34)


#Convertir un tipo de dato int astr
numero_str=str(numero)
print(texto+" "+numero_str)

print(texto+" "+str(numero)) #Es la mas comun para mostrar una cadena con algo que no es cadena 

#CONVERTIR UN STR A INT

n1=33
suma=int('23')+n1
print("la suma: "+str(suma))

#Convertir un float a int
print(" ")
n1=33
n2=int(33.99)
suma=n1+n2
print(suma)

#Convertir un int a float
n1=3
n2=4


suma=n1+n2
print(f"la suma es: {suma}")
print("la suma es: "+str(suma))

