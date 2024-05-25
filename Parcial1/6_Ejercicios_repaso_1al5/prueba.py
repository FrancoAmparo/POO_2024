while True:
    nombre = input("Nombre del trabajador: ")
    horas_trabajadas = float(input("Horas trabajadas por día: "))
    dias_trabajados = int(input("Días trabajados: "))
    sueldo_por_hora = float(input("Sueldo por hora: "))

    sueldo_semanal = horas_trabajadas * dias_trabajados * sueldo_por_hora
    sueldo_mensual = sueldo_semanal * 4

    if sueldo_mensual <= 10000:
            categoria = "Obrero tipo A"
    elif 10000 < sueldo_mensual < 15000:
            categoria = "Obrero tipo B"
    else:
            categoria = "Sin categoría"

    trabajador = {
    "nombre": nombre,
            "sueldo_semanal": sueldo_semanal,
            "sueldo_mensual": sueldo_mensual,
            "categoria": categoria
        }
    otra_captura = input("¿Deseas otra captura? (si/no): ")
    if otra_captura != 'si':
        break
if otra_captura!= "si":
    i=0
   
    total_sueldo=0
    print(f"\nTrabajador {i}:")
    print(f"Nombre: {trabajador['nombre']}")
    print(f"Sueldo semanal: {trabajador['sueldo_semanal']}")
    print(f"Sueldo mensual: {trabajador['sueldo_mensual']}")
    print(f"Categoría: {trabajador['categoria']}")
    total_sueldo += trabajador['sueldo_mensual']
    i+=-1
    print(f"\nTotal de trabajadores capturados: {i}")
    print(f"Total de sueldos mensuales: {total_sueldo:}")
    print()