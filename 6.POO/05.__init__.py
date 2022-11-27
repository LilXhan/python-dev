# POR DEFAULT


class User:
    # Object -> todas las clases de python heredan de la clase Object, clase que posee el metodo init 
    def __init__(self):
        self.username = ''
        self.password = ''

user1 = User()
user2 = User()
user3 = User()

print(user1.__dict__) # {'username': '', 'password': ''}
print(user2.__dict__) # {'username': '', 'password': ''}
print(user3.__dict__) # {'username': '', 'password': ''}


# PERSONALIZANDO ATRIBUTOS

class Person:
    def __init__(self, username='', password=''):
        self.username = username
        self.password = password

person1 = Person('person1', 'secret1')
person2 = Person('person2', 'secret2')
person3 = Person('person3', 'secret3')
person4 = Person()

print(person1.__dict__) # {'username':'person1', 'password': 'secret1'}
print(person2.__dict__) # {'username':'person2', 'password': 'secret2'}
print(person3.__dict__) # {'username':'person3', 'password': 'secret3'}
print(person4.__dict__) # {'username': '', 'password': ''}