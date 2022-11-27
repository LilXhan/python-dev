class Mascota: # Clase Padre
    

    def comer(self):
        print('la mascota come')

    def dormir(self):
        print('la mascota duerme') 



# class <clase(clase la cual queremos heredar)> -> haciendo esto: los objetos de tipo perro, facilmente
# podran acceder a todos los atributos y metodos de la clase Mascota

# Una clase puede convertirse en clase padre una n cantidad de veces

class Perro(Mascota): # Clase Hija
    pass

class Gato(Mascota):
    pass

duke = Perro()
duke.comer()
duke.dormir()


gatuno = Gato()
gatuno.comer()
duke.dormir()