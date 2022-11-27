class Animal:

    def comer(self):
        print('La animal duerme.')
    

class Mascota(Animal):
    pass


class Felino:

    def cazar(self):
        print('El felino caza.')


class Gato(Mascota, Felino):
    pass


patricio = Gato()
patricio.cazar()
patricio.comer()