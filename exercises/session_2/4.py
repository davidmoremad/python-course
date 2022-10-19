# Estudiémos los bucles. Dado el siguiente diccionario, imprime cada categoria y sus elementos.
# De forma que la salida del programa debería ser similar a lo siguiente:
#
#   peliculas
#       (2000) Title: El Padrino
#       (2000) Title: El Padrino II
#       (2000) Title: El Padrino III
#   libros
#       (2000) Title: El Señor de los Anillos
#       (2000) Title: El Hobbit
#       (2000) Title: El Silmarillion
#   ...

favoritos = {
    'peliculas': [
        {'title': 'El Padrino', 'year': 2000},
        {'title': 'El Padrino II', 'year': 2000},
        {'title': 'El Padrino III', 'year': 2000}
    ],
    'libros': [
        {'title': 'El Señor de los Anillos', 'year': 2000},
        {'title': 'El Hobbit', 'year': 2000},
        {'title': 'El Silmarillion', 'year': 2000}
    ],
    'series': [
        {'title': 'Breaking Bad', 'year': 2000},
        {'title': 'The Wire', 'year': 2000},
        {'title': 'The Sopranos', 'year': 2000}
    ],
    'canciones': [
        {'title': 'Fly me to the moon', 'year': 2000},
        {'title': 'The sound of silence', 'year': 2000},
        {'title': 'Imagine', 'year': 2000}
    ],
    'videojuegos': [
        {'title': 'GTA 5', 'year': 2000},
        {'title': 'The Witcher 3', 'year': 2000},
        {'title': 'The Last of Us', 'year': 2000}
    ],
}

def print_element(element):
    print(f"\t({element['year']}) Title: {element['title']}")

def main():
    # Introduce aquí tu código

main()