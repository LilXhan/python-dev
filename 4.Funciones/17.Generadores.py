# Un generador un tipo especial de funcion la cual retorna objetos que facilmente podemos iterar
# su principal ventaja es el consumo de memoria, yield nos permite retorna un valor y nos permite
# suspender de forma momentanea la ejecucion de una funcion, no es hasta que el generador es 
# nuevamente llamada y se reanuda desde el punto en que se quedo

# recomendado para colecciones de miles, cientos de miles y millones de datos

def pares(): # generador -> Lazy Iterator (Distribucion Perezosa) 
    for n in range(0, 8, 2):
        yield n # La funcion suspende su ejecucion

        print('se reanuda la funcion')

generador = pares()

while True:
    try: 
        par = next(generador)
        print(par)
    except StopIteration: 
        print("Termino de funcion")
        break