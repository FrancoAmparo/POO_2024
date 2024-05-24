# 10.- Crear un programa que solicite la calificacion de 15 alumnos e imprimir en pantalla cuantos aproboron y cuantos no aprobaron


aprobados = 0
no_aprobados = 0


for i in range(1, 16):
    calificacion = float(input(f"Introduce la calificación del alumno {i}: "))

    if calificacion >= 5:
        aprobados += 1
    else:
        no_aprobados += 1


print(f"Total de alumnos que aprobaron: {aprobados}")
print(f"Total de alumnos que no aprobaron: {no_aprobados}")
print( )