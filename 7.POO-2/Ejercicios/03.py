"""
Cree una clase Punto con los siguientes atributos: X, Y

Cree el método mostrar_punto, el cual imprime lo siguiente.

El punto está en ( "X", "Y" )
Luego realice la composición con la clase figura creada anteriormente.

Nota:

Utilice el método mostrar_punto dentro de mostrar_figura
Utilice los mismos datos del ejercicio anterior
Cree un objeto Figura y llame a mostrar_figura, luego elimine el objeto.
"""


class Figura():


    def __init__(self, name, area, x, y):
        self.name = name
        self.__area = area
        self.point = Point(x, y)

    def __del__(self):
        print('figura eliminado')

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
        print(f'La figura se llama {self.name}')
        print(f'Tiene un área de {(self.__area)}m²')
        self.point.show_point()


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    
    def __del__(self):
        print('point eliminado')


    def show_point(self):
        print(f'El punto esta en ({self.x}, {self.y})')


circulo = Figura('Circulo', 30.5, -1, 2)
circulo.mostrar_figura()