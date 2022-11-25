# Scope
# Para python la variable animal de la linea 4 y la variable animal de la linea 7 son objetos completamente
# diferentes, ya que estas variables fueron creadas en scopes diferentes

animal = 'León' # -> Variable global (Pueden ser utilizadas dentro de cualquier bloque -> Función
# condicion o ciclo)

def imprimir_animal():

    # global animal  -> con esto le decimos a python que usaremos la variable global y con esto podremos 
    # modificar su valor

    animal = 'Ballena' # -> Variable local (Unicamente puede ser utilizada dentro del bloque donde fue creada)

    tipo = 'Mamifero' # -> Variable local

    print(animal) # Ballena
    print(id(animal)) # ....88

imprimir_animal()

print(animal) # Léon
print(id(animal)) # ....60

# print(tipo) -> error