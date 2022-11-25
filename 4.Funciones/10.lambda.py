# Una funcion lambda -> funcion anonima
# no es mas que una funcion la cual es expresada en una sola linea de codigo ademas de no poseer un nombre
# ya que comúnmente este tipo de funciones realizan tareas muy pequeñas

# lambda <parámetros> : <cuerpo de la función)
funcion_grados = lambda celcius : celcius * 1.8 + 32 

print(funcion_grados(10))

sin_parametros = lambda : True
parametros_default = lambda p1=10, p2=20, p3=30 : p1 + p2 + p3
asterisco = lambda *args, **kwargs: len(args) + len(kwargs)

