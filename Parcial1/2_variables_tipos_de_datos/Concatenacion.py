#Formas de concatenar en python 

nombre="Amparo Franco"
especialidad= "Area de software multiplataforma"
carrera= "Ingenieria en gestion de desarrollo de software"

#Primer forma
print("Mi nombre es"+nombre+"estoy en la especialidad"+especialidad+" y estudio la carrera de"+carrera)

print("\n")

#segunda forma
print("Mi nombre es",nombre, "estoy en la especialidad",especialidad, " y estudio la carrera de",carrera)

print("\n")

#Tercera forma mas comun en python
print(f"Mi nombre es,{nombre}, estoy en la especialidad,{especialidad},  y estudio la carrera de ,{carrera}")

print("\n")

#cuarta forma
print("Mi nombre es,{}, estoy en la especialidad,{},  y estudio la carrera de ,{}". format(nombre, especialidad, carrera))

print("\n")

#quinta forma
print('Mi nombre es'+nombre+'estoy en la especialidad'+especialidad+' y estudio la carrera de'+carrera)

print("\n")
print("" )
