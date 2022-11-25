
promedio = lambda *args : sum(args) /  len(args)

aprobatorio = lambda calificacion : calificacion >= 7

print(promedio(1, 3, 4, 5, 6, 7, 8)) # -> 4.8
print(aprobatorio(7)) # -> True
print(aprobatorio(5)) # -> False

def aprobatorio(calificacion):
    return calificacion >= 90

def mostrar_mensaje(func_promedio, func_aprobatorio, *args):
    promedio = func_promedio(*args)

    if func_aprobatorio(promedio):
        print(f"Felicidades aprobaste la materia con: {promedio}")
    else:
        print("No aprobaste la materia.")


# callbacks -> funciones pasados por parametros o argumentos
# sirven para moduralizar nuestro pograma

mostrar_mensaje(promedio, aprobatorio, 10, 10, 20)