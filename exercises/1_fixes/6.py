# Corrige el error para que la salida del programa sea correcta

clientes = [
    {'nombre': 'Sergio', 'edad': 29, 'sexo': 'M'},
    {'nombre': 'David', 'edad': 29, 'sexo': 'M'},
    {'nombre': 'Alicia', 'edad': 52, 'sexo': 'F'},
]

for cliente in clientes:
    if cliente == 'M':
        print(f'{cliente["nombre"]} tiene {cliente["edad"]} años y es varón')
    else:
        print(f'{cliente["nombre"]} tiene {cliente["edad"]} años y es mujer')