# Los atributos de clase, no seran mas que atributos los cuales le pertenezcan a una clase, y para que nosotros
# podamos utilizarlos obligatoriamente tenemos que utilizar dicha clase

# Para crear un atributo de clase, tan solo basta con crear variables dentro de la clase:

class User:
    username = ''
    email = ''

print(User.username) # -> asi podemos utilizar los atributos de clase <clase.atributo>

# Podemos consultar o modificarlo un atributo de clase

User.username = 'Flavio'
User.email = '@gmail.com'
print(User.username)
print(User.email)
