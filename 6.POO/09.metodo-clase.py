# METODOS DE CLASE -> OBJETOS

class Circulo:

    pi = 3.141592

    @classmethod
    def area(cls, radio):
        return cls.pi * (radio ** 2)


result = Circulo.area(5)
print(result)