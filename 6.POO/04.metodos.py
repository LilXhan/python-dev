# Para que nosotros podamos crear metodos dentro de nuestras clase, 
# basta con definir funciones dentro de la clase.

# para que una funcion pueda considerarse un metodo obligatoriamente debe poseer un parametro
# parametro el cual hace referencia al objeto que llama al metodo -> por convencion este parametro
# tendra por nombre self haciendo referencia 'sigo mismo' o 'uno mismo'



class Usuario:
    # metodo inicializar
    # self -> objeto
    def inicializar(self, username, password):
        # Añadimos atributos al objeto
        # el parametro self toma al objeto o al objeto perse (user1 o user2)
        self.username = username
        self.password = password

user1 = Usuario()
user2 = Usuario()
user3 = Usuario()

print(user1.__dict__) # vacio
print(user2.__dict__) # vacio

########################################

# Usamos el metodo inicializar para crear nuestros atributos de nuestros objetos

user1.inicializar('user1', 'secret1')
user2.inicializar('user2', 'secret2')
user3.inicializar('Flavio', 'contraseña123')

print(user1.__dict__) # {username: 'user1', password: 'secret1'}
print(user2.__dict__) # {username: 'user2', password: 'secret2'}
print(user3.__dict__) # {username: 'Flavio', password: 'contraseña123'}