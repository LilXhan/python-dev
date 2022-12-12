class SerVivo():

    def dormir(self):
        print('El servivo duerme')


class Animal(SerVivo):

    def comer(self):
        print('El animal esta comiendo.')




class Mascotas(Animal):
    
    def comer(self):
        super().comer()
        print('La mascota come')

class Felino():

    def cazar(self):
        pass

class Gato(Mascotas, Felino):
    
    def __init__(self, name):
        self.name = name

    def comer(self):
        super().comer()
        print(f'{self.name} come.')


patricio = Gato('Patricio')

patricio.comer()
patricio.dormir()