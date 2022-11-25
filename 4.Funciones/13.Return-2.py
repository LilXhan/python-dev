# retornando funciones y guardandolas en una variable

def saludar():

    
    def mostrar_mensaje():
        print("Hola nos encontramos en el curso de Python.")
    
    return mostrar_mensaje


respuesta = saludar()

respuesta() # -> Hola nos encontramos en el curso de Python.
