# Al agregar un asterisco al inicio del parametro, le decimos a python que todos los argumentos utilizados
# al momento de llamar a la funcion van a servir para generar una tupla, tupla la cual se va a asignar
# al parametro que tenga el asterisco 

def avg_numbers(*args):
    print(type(args)) # tuple
    return sum(args) / len(args)

promedio = avg_numbers(1, 2, 3, 10, 10)
print(promedio)


# El uso del asterisco no nos limita para usar otros argumentos

def combinacion(p1, p2, *args, p4=500):
    print(p1) # 10
    print(p2) # 20
    print(args) # (1, 2, 3, 4, 5, 6)
    print(p4) # 1000


combinacion(10, 20, 1, 2, 3, 4, 5, 6, p4=1000)