"""
Cree la clase Circulo la cual herede de la clase Figura, adicione los siguientes atributos:

Radio
Centro X
Centro Y
Nota: Con centro "X" y "Y", agregue una composición con la clase Punto.

Cree el método mostrar_circulo, el cual haga uso de mostrar_figura, además agregue las siguientes impresiones:

El círculo tiene un radio de "Radio"
Centro:
El punto de inicio esta en ( "Centro X", "Centro Y" )
Nota:

Para el centro utilice mostrar_punto
Utilice los mismo datos del ejecicio 3 y adicione lo siguiente.
Radio = 3
Centro X = 2
Centro Y = 3
Cree un objeto circulo, llame a mostrar_circulo y luego elimine el objeto
"""

class Figura():

    def __init__(self, nombre, area, x, y):
        self.nombre = nombre
        self.__area = area
        self.x = x
        self.y = y
        self.point = Point(x, y)
       

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

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        

    def show_point(self):
        print(f'El punto esta en ({self.x}, {self.y})')


class Circle(Figura):

    def __init__(self, nombre, area, x, y, center_x, center_y, radio):
        self.center_x = center_x
        self.center_y = center_y
        self.radio = radio
        super().__init__(nombre, area, x, y)

    def __del__(self):
        print('cuadrado eliminado')

    def mostrar_circulo(self):
        self.mostrar_figura()
        print(f'El circulo tiene un {self.radio}')
        self.point.show_point()
        print(f'El punto de inicio esta en ( "{self.center_x}", "{self.center_y}" )')


    
circulo = Circle('Circulo', 30.5, -1, 2, 2, 3, 3)
circulo.mostrar_circulo()
    
    