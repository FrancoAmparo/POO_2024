#5.- Hacer un programa que muestre todos los numeros entre 2 numeros que diga el usuario


num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))


if num1 > num2:
    num1, num2 = num2, num1


if num1 == num2:
    print(f"No hay números entre {num1} y {num2} porque son iguales.")
elif num1 + 1 == num2:
    print(f"No hay números entre {num1} y {num2}.")
else:
   
    print(f"Todos los números entre {num1} y {num2} son:")
    for num in range(num1 + 1, num2):
        print(num)

