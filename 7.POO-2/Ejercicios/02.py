"""
Cree una clase Automovil con los siguientes atributos.

Marca
Año
Placa
Número de Asientos
Escriba los getters y setter del atributo marca.

Cree dos métodos, mostrar_carro y tipo_carro.

mostrar_carro imprime:

El carro es de marca "Marca" del año "Año"
Y tiene placa número "Placa"
tipo_carro imprime:

Si el número de asientos es mayor a 20, imprimir:

El automóvil es un bus.
Si el número de asientos es mayor a 10, imprimir:

El automóvil es una combi.
Si no, imprimir:

El automóvil es un carro normal
Crear un objeto con los siguientes datos, y llamar a los métodos creados.

Marca = Suzuki
Año = 2010
Placa = ABC-456
Número de Asientos = 4
"""

class Automovil():

    def __init__(self, brand, age, id, num_seats):
        self.__brand = brand
        self.age = age
        self.id = id
        self.num_seats = num_seats


    def __del__(self):
        print('autmovil eliminado')
        

    @property
    def brand(self):
        return self.__brand


    @brand.setter
    def brand(self, brand):
        self.__brand = brand


    def show_car(self):
        print(f'El carro es de marca {self.marca} del año {self.age} y tiene el número de placa {self.id}')


    def type_car(self):
        if self.num_seats > 20:
            print('El autmovil es un bus')
        elif self.num_seats > 10:
            print('El automovil es una combi')
        else:
            print('El carro es uno normal')


my_car = Automovil('Suzuki', 2010, 'ABC-456', 4)

my_car.show_car()
my_car.type_car()