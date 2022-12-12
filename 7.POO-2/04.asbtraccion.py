class Lavadora:

    def __init__(self):
        pass

    
    def lavar(self, temperatura='caliente'):
        self._llenar_tanque_de_agua(temperatura)
        self._add_jabon()
        self._lavar()
        self._centrigar()

    
    def _llenar_tanque_de_agua(self, temperatura):
        print(f'Llenando el tanque de agua {temperatura}')
    

    def _add_jabon():
        print('Añadiendo jabon')


    def _lavar():
        print('Lavando ropa')


    def _centrifugar():
        print('Centrigurando')