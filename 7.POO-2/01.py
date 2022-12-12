
class Persona():

    def __init__(self, name, edad):
        self.name = name
        self.edad = edad

    
    def saludar(self, objeto_otra_persona):
        print(f"{self.name} saluda a {objeto_otra_persona.name}")


david = Persona('David', 15)
flavio = Persona('Flavio', 16)

flavio.saludar(david)