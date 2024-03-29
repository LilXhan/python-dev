# COORDENADA

class Coordenada:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    
    def distancia(self, otra_coordenada):
        x_diff = (self.x - otra_coordenada.x) ** 2
        y_diff = (self.y - otra_coordenada.y) ** 2
        
        return (x_diff + y_diff) ** 0.5


if __name__ == '__main__':
    coord_1 = Coordenada(1, 10)
    coord_2 = Coordenada(20, 3)

    result = coord_1.distancia(coord_2)
    print(result)

    print(isinstance(coord_1, Coordenada)) # -> coord_1 si es instancia de Coordenada
    print(isinstance(coord_2, Coordenada)) # -> coord_2 si es instancia de la clase Coordenada

    print(isinstance(3, Coordenada)) # -> False 3 no es instancia de Coordenada