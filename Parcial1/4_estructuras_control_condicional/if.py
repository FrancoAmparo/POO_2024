#Esta estructura de control evalua una condicion si la condicion se cumple se ejecuta la o las intrucciones contenidas dentro de ella

#Esta estructura tiene 4 variantes 
#1 if simple
#2 if compuesto
#3 if anidado
#4 if con el elif 

#Ejemplo 1 if simple

#if color=="rojo":
#print("Soy el color rojo")

#Ejemplo 2 if compuesto

#if color=="rojo":
#print("Soy el color rojo")
#else:
#print("No soy el color rojo ")

#Ejemplo 3 if anidado

#if color=="rojo":
#print("Soy el color rojo")
#if color!= ("no soy rojo"):
#else:
#print("No soy el color rojo ")

#Ejemplo 4 if y elif

#if color=="rojo":
#print("Soy el color rojo")
#elif color=="amarillo":
#print("No soy el color amaillo ")
#elif color=="azul":
#print("soy el color negro ")
#else:
#print("no soy niguno de los colores anteriores")


color=input("ingresa el color: ")
if color=="rojo":
     print("Soy el color rojo")
elif color=="amarillo":
       print("No soy el color amaillo ")
elif color=="azul":
     print("soy el color negro ")
else:
      print("no soy niguno de los colores anteriores")