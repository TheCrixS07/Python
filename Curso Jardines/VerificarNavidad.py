'''3. Verificar Navidad: Crear un programa que pida una fecha y verifique si corresponde a Navidad (25 de diciembre).'''

fecha = input("Ingrese una fecha con el siguiente formato DD/MM: ")

if fecha == "24/12":
    print(f"La fecha ingresada {fecha} es Navidad")
else:
    print(f"La fecha ingresada {fecha} no es Navidad")