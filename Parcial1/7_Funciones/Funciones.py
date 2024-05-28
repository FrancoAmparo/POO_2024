#Una funcion e sun conjunto de instrucciones agrupadas bajo un nombre en particular como un programa más pequeño que cumple una funcion especifica. La funcion se puede reutilizar con el simple hecho de invocarla, es decir mandarla a llarmer


#Sintaxis

#def nombredeMifuncion(parametros):

#bloque o conjunto de instrucciones

#nombredeMifuncion(parametros)

#Las funciones pueden ser de 4 tipos
#   1.- Funcion que no recibe parametros y no regresa valor 
#   2.- Funcion que no recibe parametros y regresa valor
#   3.- Funcion que recube parametros y no regresa valor
#   4.- Funcion que recibe parametros y regresa valor


#Ejemplo 1: Crear una funcion para imprimir nombres de personas
#FUNCION QUE NO RECIBE PARAMETROS Y NO REGRESA VALOR
def solicitarNombres():
    nombre=input("Ingresa el nombre completo: ")


solicitarNombres()




#Ejemplo 2: Crear una funcion que realice la sumatoria de 2 numeros
#FUNCION QUE NO RECIBA PARAMETROS Y REGRESA VALORES
def suma():
    n1=int(input("Numero #1: "))
    n2=int(input("Numero #2: "))
    suma=n1+n2
    print(f"{n1}+{n2}={suma}")


suma()


#Ejemplo 3: usar dos numeros 
#FUNCION QUE NO RECIBA PARAMETROS Y REGRESA VALORES
def suma():

    n1=int(input("Numero #1: "))
    n2=int(input("Numero #2: "))
    suma=n1+n2
    return suma


resultado_suma=suma()
print("La suma es:  {resultado_suam}")  #opcion 1



#Ejemplo #4 
#FUNCION QUE RECIBE PARAMETROS Y NO REGRESA VALOR

def suma(n1,n2):
    suma=n1+n2
    print(f"La suma es: {suma}")

n1=int(input("Numero #1: "))
n2=int(input("Numero #2: "))
suma(n1,n2)



#Ejemplo #5
#FUNCION QUE RECIBE PARAMETROS Y REGRESA VALORES
#MAAAAAAS USADOOO?
def suma(n1,n2):
    suma=n1+n2
    return suma
n1=int(input("Numero #1: "))
n2=int(input("Numero #2: "))
resultado_suma=suma(n1,n2)
print(f"La suma es: {resultado_suma}")

print((f"{n1}+{n2}={suma(n1,n2)}"))




#Ejemplo #6: Crear un programa que solicite a traves de una funcion la sig informacion
#nombre del paciente, edad, estatura, tipo de sangre
#Utilizar los 4 tipós

#1
#Funcion que no recibe parametros y no regresa valor 

def paciente():
    nombre=input("Ingrese el nombre completo: ")
    edad=input("Ingrese la edad: ")
    estatura=input("Ingrese la estatura: ")
    tipo_sangre=input("Ingrese el tipo de sangre: ")

paciente()


#2
#Funcion que no recibe parametros y regresa valor