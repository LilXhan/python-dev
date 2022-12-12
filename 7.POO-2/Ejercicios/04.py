"""
Cree la clase Rueda con los siguientes atributos:

Marca = Michelin
Índice de carga = 16
Diámetro = 99
Cree el método mostrar_llanta, que imprima lo siguiente:

La llanta es de marca "Marca"
El índice de carga es de "Índice de carga"
Y tiene un diámetro de "Diámetro"
Realice la composición con la clase Automovil.

Notas:

Utilice mostrar_llanta dentro del método tipo_carro
Utilice los datos del Problema 2
Cree un objeto automovil, use mostrar_llanta y luego elimine el objeto
"""

class Automovil():

    def __init__(self, brand, age, id, num_seats):
        self.__brand = brand
        self.age = age
        self.id = id
        self.num_seats = num_seats
        self.wheel = Wheel(brand, 12, 20)


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



automovil = Automovil('Suzuki', 2010, 'ABC-456', 4)
automovil.wheel.show_wheel()