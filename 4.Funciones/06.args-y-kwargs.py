def combinacion(*args, **kwargs):
    print(args) # (1, 2, 3, 4, 5)
    print(kwargs) # {'cody': True, 'curso': 'Python'}


combinacion(1, 2, 3, 4, 5, cody=True, curso='Python')

