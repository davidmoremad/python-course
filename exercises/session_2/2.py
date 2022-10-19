# El código de este programa funciona correctamente, pero podría ser más legible y eficiente. ¿Cómo lo harías?

fav_films = [
    {'title': 'Trainspotting', 'author': 'Danny Boyle', 'year': 1996, 'genre': 'Drama'},
    {'title': 'Matrix', 'author': 'Wachowski', 'year': 1999, 'genre': 'Sci-Fi'},
    {'title': 'Captain Fantastic', 'author': 'Matt Ross', 'year': 2016, 'genre': 'Dramedy'}
]
fav_songs = [
    {'title': '72 hookers', 'author': 'NOFX', 'year': 2012, 'genre': 'Punk'},
    {'title': 'Monkey Wrench', 'author': 'Foo Fighters', 'year': 1997, 'genre': 'Rock'},
    {'title': 'Whats my age again', 'author': 'Blink182', 'year': 1999, 'genre': 'Pop Punk'}
]
fav_books = [
    {'title': 'Sapiens', 'author': 'Yuval Noah', 'year': 2011, 'genre': 'Not-fiction'},
    {'title': 'El mundo de Sofia', 'author': 'Jostein Gaarder', 'year': 1999, 'genre': 'Novel'},
    {'title': 'The prince', 'author': 'Maquiavelo', 'year': 1532, 'genre': 'Not-fiction'}
]


# Mostrando mis peliculas favoritas
print('\n[+] Favorite films:')
for film in fav_films:
    print('\t{year} - \"{title}\" by {author}'.format(**film))

# Mostrando mis canciones favoritas
print('\n[+] Favorite songs:')
for song in fav_songs:
    print('\t{year} - \"{title}\" by {author}'.format(**song))

# Mostrando mis libros favoritos
print('\n[+] Favorite books:')
for book in fav_books:
    print('\t{year} - \"{title}\" by {author}'.format(**book))