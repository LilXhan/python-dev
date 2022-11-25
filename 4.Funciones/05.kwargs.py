def usuario(**kwargs):
    print(type(kwargs)) # dict
    print(kwargs) # {'eduardo': [10, 10, 8], 'fernando': [10, 10, 9]}


usuario(eduardo=[10, 10, 8], fernando=[10, 10, 9])
