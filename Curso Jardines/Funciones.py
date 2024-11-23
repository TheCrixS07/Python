'''Escribe una función llamada convertir_celsius_a_fahrenheit que reciba un valor en grados Celsius 
y devuelva su equivalente en Fahrenheit.'''

def convertir_celsius_fahrenheit(celsius):
    fahrenheit = (celsius * (9/5))+32
    return fahrenheit


print(convertir_celsius_fahrenheit(30))