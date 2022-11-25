
e = 'e' # variable global

def funcion_principal():
    a = 'a' # variable local
    b = 'b' # variable local

    def funcion_anidada ():

        c = 'c' # variable local

        nonlocal b # -> le decimos a python que vamos vamos a usar la variable b de un scope
        # mas arriba de este y asi poder modificarla

        b = 'Cambio de valor'

        print(a) # a
        print(b) # 'Cambio de valor'
        print(id(b)) # ....05

        print(e) # e
    
    funcion_anidada()
    print(b) # 'Cambio de valor'
    print(id(b)) # ....05

