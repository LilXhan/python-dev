
class Automovil:

    def __init__(self, modelo='b550', marca='hyndai', color='negro'):
        self.modelo = modelo
        self.marca = marca 
        self._color = Carroseria(marca='toyota')
        self._estado = 'en reposo'
        self._motor = Motor(cilindros=4)


    def acelerar(self, tipo='despacio'):
        if tipo == 'rapida':
            self._motor.inyecta_gasolina(10)
        else:
            self._motor.inyecta_gasolina(3)

        self._estado == 'movimiento'

    def color(self, metalizado, marca, color):
        if metalizado:
            self._color.seleccionar_color(marca=marca, color=color, metalizado=True)
        else:
            self._color.seleccionar_color(marca=marca, color=color, metalizado=False)

class Motor:

    def __init__(self, cilindros, tipo='gasolina'):
        self.cilindros = cilindros
        self.tipo = tipo
        self._temperatura = 0

    
    def inyecta_gasolina(self, cantidad):
        pass


class Carroseria:

    def __init__(self, color='negro', marca='hyundai'):
        self.color = color


    def seleccionar_color(self, marca, color, metalizado=False):
        if metalizado:
            print(f'El carro de marca {marca} es de color {color} metalizado')
        else:
            print(f'El carro de marca {marca} es de color {color}')


auto = Automovil()
print(auto.color(False, 'toyota', 'rojo')) # -> el carro de marca toyota es rojo metalizado
