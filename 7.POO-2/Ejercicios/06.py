"""
Cree la clase Bus que herede de la clase Automovil y adicione los siguientes atributos:

Tipo de uso
Empresa
Cree el método "mostrar_bus", el cual haga uso de "mostrar_carro" y "tipo_carro" de la clase automovil, además agrege la siguiente impresión.

El autobus se usa para transporte "Tipo de uso"
La empresa a la que pertenece es: "Empresa"
Notas:

Use mostrar_carro y tipo_carro dentro de mostrar_bus

Use los datos del ejecicio 4 y adicione lo siguiente:

Tipo de uso = escolar
Empresa = Empress
"""


class Automovil():

    def __init__(self, brand, age, id, num_seats):
        self.__brand = brand
        self.age = age
        self.id = id
        self.num_seats = num_seats
        self.wheel = Wheel(brand, 12, 20)




    @property
    def brand(self):
        return self.__brand


    @brand.setter
    def brand(self, brand):
        self.__brand = brand


    def show_car(self):
        print(f'El carro es de marca {self.brand} del año {self.age} y tiene el número de placa {self.id}')


    def type_car(self):
        if self.num_seats > 20:
            print('El autmovil es un bus')
        elif self.num_seats > 10:
            print('El automovil es una combi')
        else:
            print('El carro es uno normal')
        self.wheel.show_wheel()

class Wheel:

    def __init__(self, brand, load_index, diameter):
        self.brand = brand
        self.load_index = load_index
        self.diameter = diameter

    def __del__(self):
        print('llanta eliminado')


    def show_wheel(self):
        print(f"La llanta es de marca {self.brand}")
        print(f"El indice de carga es de {self.load_index}")
        print(f"Tiene un diametro de {self.diameter}")


class Bus(Automovil):

    def __init__(self, brand, age, id, num_seats, type_use, enterprise):
        self.type_use = type_use
        self.enterprise = enterprise
        super().__init__(brand, age, id, num_seats)


    def __del__(self):
        print('bus eliminado')

    
    def show_bus(self):
        self.show_car()
        self.type_car()
        print(f'Tipo de uso: {self.type_use}')
        print(f'Empresa: {self.enterprise}')


bus = Bus('Suzuki', 2010, 'ABC-456', 4, 'escolas', 'espress')
bus.show_bus()
