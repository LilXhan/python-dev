"""
Dada la lista de notas [15,20,18] y la lista de alumnos ["Marcelo", "José", "Juan"], 
imprimirlos de la siguiente forma:

1 -> Jose : 20

2 -> Juan : 18

3 -> Marcelo : 15
No usar range, ni comparadores. Hint: usar sorted
"""

def merito(notas, alumnos):
    dict_notas = {alumno : nota for nota, alumno in zip(notas, alumnos)}

    dict_notas_sorted = dict(sorted(dict_notas.items(), key=lambda x:x[1], reverse=True)) # ordenando con sorted un diccionario

    for index, key in enumerate(dict_notas_sorted):
        nota = dict_notas[key] 
        print(f"{index} -> {key} : {nota}")

merito([15, 20, 18], ['Marcelo', 'José', 'Juan'])
