"""
Dada la lista de notas [15,20,18] y la lista de alumnos ["Marcelo", "José", "Juan"] 
Imprimirlos de la siguiente forma:

Marcelo : 15

José : 20

Juan : 18
"""

def alumnos(notas, alumnos):
    for nota, alumno in zip(notas, alumnos):
        print(f"{alumno}: {nota}")

alumnos([15, 20, 18], ['Marcelo', 'José', 'Juan'])