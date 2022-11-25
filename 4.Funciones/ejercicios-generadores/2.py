"""
Dada la siguiente lista ['Hola', True, 5, 6.04]

Imprimir los valores e índices sin utilizar un contador o range.

0 -> Hola
1 -> True
2 -> 5
3 -> 6.04
"""


def index(*args):
    for index, arg in enumerate(args):
        print(f"{index} -> {arg}")


index('Hola', True, 5, 6.04)
        