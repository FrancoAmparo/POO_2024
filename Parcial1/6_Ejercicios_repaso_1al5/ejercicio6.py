#6.- Mostrar todas las tablas del 1 al 10. Mostrando el titulo de la tabla y luego las multiplicaciones del 1 al 10



multi=0
b=1

for b in range(1,11):
     for i in range(1,11):
         multi=i*i
         print(f"{b} X {i} = {multi}")