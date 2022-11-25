# En terminos simples un closure no es mas que una funcion la cual puede generar de forma dinamica a otra
# funcion, y esta nueva funcion puede acceder a las variables locales aun cuando hayan finalizado 

def saludar(username):
    mensaje = f"Hola {username}" # Variable Local

    def mostrar_mensaje(): # Anidada
        print(mensaje)

    return mostrar_mensaje


username = 'Flavio'
respuesta = saludar(username)

respuesta()