
"""
  Para crear una funcion usamos la palabra reservada def
"""

def suma():
    numero_uno = int(input("Ingresa el primer número entero:\n"))
    numero_dos = int(input("Ingresa el segundo número entero:\n"))

    resultado = numero_uno + numero_dos
    print(resultado)

# se pueden llamar las veces que queramos

# suma()

# Pasando como parametros

numero_uno = int(input("Ingresa el primer número entero:\n"))
numero_dos = int(input("Ingresa el segundo número entero:\n"))

def suma_dos(numero_uno, numero_dos):
    resultado = numero_uno + numero_dos
    print(resultado)



