def suma(n1, n2):
    return n1 + n2

numero_uno = int(input("Ingrese número 1:\n"))
numero_dos = int(input("Ingrese número 2:\n"))

resultado = suma(numero_uno, numero_dos)

print(resultado)

############################################################################################################

def suma(n1, n2):
    return n1 + n2, 'La funcion retorna 2 valores'

numero_uno = int(input("Ingrese número 1:\n"))
numero_dos = int(input("Ingrese número 2:\n"))

resultado, mensaje = suma(numero_uno, numero_dos)

print(f"El resultado es: {resultado}")
print(mensaje)