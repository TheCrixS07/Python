'''1. Mayor de Tres Números: Cargar tres números distintos por teclado y mostrar cuál es el mayor.'''

num = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))
num3 = int(input("Ingrese el tercer numero: "))

if num > num2 and num > num3:
    print(f"El primer numero es mayor {num}")
elif num2 > num and num2 > num3:
    print(f"El segundo numero es mayor {num3}")
else:
    print(f"El tercer numero es mayor {num3}")
