# un decorador no es mas que una funcion que toma como input una funcion y a la vez retorna una funcion
# al momento de trabajar con un decorador estaremos trabajando con 3 funciones


"""
a -> la funcion principal (Decorador)
b -> la funcion a decorar
c -> la funcion decorada

siempre usaremos decoradores cuando quedramos extender funcionalidades a una funcion
"""

def funcion_a(funcion_b):

    def funcion_c():
        print('antes del llamado')
        funcion_b()
        print('despues del llamado')

    return funcion_c

@funcion_a
def saludar():
    print("hola nos encontramos en una función.")


@funcion_a
def suma():
    print(10 + 30)

saludar() # se ejecuta la funcion decorada no la a decorar
suma()

