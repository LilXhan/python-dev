"""
Cree una clase figura, que tenga los siguientes atributos.

Nombre
Área
Coordenada X
Coordenada Y
Escriba sus respectivos getters y setters de área.

Y cree el método mostrar_figura, qué imprima lo siguiente:

La figura se llama "Nombre"
Tiene un área de "Área" m^2
E inicia en las coordenadas ( "X", "Y" )

Luego, cree un objeto con los siguiente datos.

Nombre = Círculo
Área = 30.5
Coordenada X = -1
Coordenada Y = 2
Llame al método mostrar_figura, y luego destruya el objeto.
"""


class Figura():

    def __init__(self, nombre, area, x, y):
        self.nombre = nombre
        self.__area = area
        self.x = x
        self.y = y
    

    def __del__(self):
        print('point eliminado')


    @property
    def area(self):
        return self.__area


    @area.setter
    def area(self, area):
        if area is int:
            self.__area = area
        else:
            msg = f'{area} no es un número'
            raise ValueError(msg)


    def mostrar_figura(self):
        print(f'La figura se llama {self.nombre}')
        print(f'Tiene un área de {(self.__area)}m²')
        print(f'E inicia con los siguientes coordenadas ({self.x}, {self.y})')


circulo = Figura('Circulo', 30.5, -1, 2)
circulo.area = 's'
circulo.mostrar_figura()