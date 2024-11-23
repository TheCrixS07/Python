'''Crea una función calcular_promedio que reciba una lista de números y devuelva el promedio. Valida que la lista no esté vacía.'''

def calcular_promedio(lista):
    if not lista:
        raise ValueError("La lista no debe estar vacia")
    return sum(lista)/len(lista)

