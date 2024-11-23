'''Desarrolla una función llamada calcular_factorial que calcule el factorial de un número entero positivo utilizando recursión. 
Asegúrate de manejar casos inválidos.'''

def calcular_factorial(numero:int)-> int:
    if not isinstance(numero, int) or numero < 0:
        raise ValueError("El numero debe ser un entero positivo")
    if numero == 0 or numero == 1:
        return 1
    return  numero *calcular_factorial(numero - 1)