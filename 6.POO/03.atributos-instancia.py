# Los atributos de instancia, no seran mas que atributos los cuales le pertenezcan a un objeto, y para
# poder utilizarlos trabajaremos con el objeto


class Usuario:
    # Atributos de clases
    username = 'Username por default'
    email = ''

# objeto = clase()

user1 = Usuario()
# 1. Verifica si el attr existe dentro del objeto si no existe  pasa al siguiente paso
# 2. Verifica si el attr existe dentro de la clase si no existe pasa al siguiente paso -> Solo lectura
# 3. Lanza un error
print(user1.username)

print(user1.__dict__) # -> con esto podremos conocer todos los atributos que posea nuestro objeto 

# Añadir atributos a nuestro objeto

user1.username = 'Pedro' # Añadimos el attributo al objeto
user1.password = '123456' # Añadimos un atributo a nuestro objeto -> cuando python nota que estamos asignando
#                           un valor a un atributo que no existe, se procede a añadir dicho atributo al objeto

print(Usuario.username) # Username por default -> atributo de clase
print(user1.username) # Pedro  -> atributo de instancia
print(user1.password) # 123456

user1.password= 'secret'
print(user1.password) # secret

print(user1.__dict__) # {username: 'Pedro', password: '123456'}

# creamos otro objeto

user2 = Usuario()

# si tratamos a acceder a password el cual se creo de forma dinamica en user1, nos dara error

print(user2.password) # -> ERROR


# No es recomendable crear atributos indiscriminadamente, se recomienda estandarizar los nombres
# de los atributos y la cantidad de atributos que va a tener un objeto a la larga vamos a obtener errores
