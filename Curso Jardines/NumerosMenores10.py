'''4. Menores a Diez: Ingresar tres números. Si todos son menores a 10, imprimir "Todos los números son menores a diez". 
Si al menos uno es menor a 10, imprimir "Alguno de los números es menor a diez".'''


num = int(input("Ingrese un numero: "))
num2 = int(input("Ingrese un numero: "))
num3 = int(input("Ingrese un numero: "))

if num < 10 and num2 < 10 and num3 < 10:
    print("Todos los numeros son menores a diez")
elif num < 10 or num2 < 10 or num3 < 10:
    print("Al menos un numero es menor a 10")
else:
    print("Los numeros no son menores a 10")