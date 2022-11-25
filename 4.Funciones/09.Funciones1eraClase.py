"""
Las funciones son ciudadanos de primera clase o tambien conocida de ciudadanos de primer orden

¿Porque?

Las funciones pueden ser asignadas a variables, pueden ser utilizadas como argumentos para otras funciones,
inclusive funciones pueden retornar funciones
"""

def celcius_to_farhenheit(celcius):
    return celcius * 1.8 + 32


mi_funcion = celcius_to_farhenheit
print(type(mi_funcion)) # <func>
print(mi_funcion(10))  # -> 50.0