# Siempre es bueno documentar nuestras funciones
# Docstring

# __doc__ (modulos, clases, metodos y funciones)


def sum(numero_1, numero_2):
    """
    La función suma 2 números enteros.

    Argumentos:
    numero_1 (int)
    numero_2 (int)

    se retorna la suma de los parametros

    TODO:
        * 
    """
    return numero_1 + numero_2


print(sum.__doc__)
print(help(sum))

