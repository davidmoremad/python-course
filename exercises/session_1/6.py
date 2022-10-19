# Corrige el error para que la salida del programa sea correcta
# El programa debe mostrar el siguiente mensaje:
#       "Sergio tiene 29 años y es varón"
#       "David tiene 29 años y es varón"
#       "Alicia tiene 52 años y es mujer"

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