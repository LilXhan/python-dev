import requests

def get_categorys():
    r = requests.get('https://api.escuelajs.co/api/v1/categories')
    print(r.status_code)
    print(r.text) # -> nos devuelve un string
    print(type(r.text)) # -> string

    # Transformando el string

    categories = r.json() # -> nos lo transforma en una lista y los elementos de adentro nos convierte en diccionarios

    for category in categories:
        print(category["name"])

