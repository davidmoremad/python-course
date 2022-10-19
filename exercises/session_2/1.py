# El código de este programa está bien, pero falta una linea para que funcione correctamente. ¿Cuál es?
# El programa debe mostrar un mensaje similar a "Receta: carne a la pimienta con patatas fritas"

carnes = ['carne de vaca', 'carne de cerdo', 'carne de pollo']
sazonados = ['pimienta', 'mantequilla', 'barbacoa', 'cerveza', 'pepitoria']
guarniciones = ['patatas fritas', 'arroz', 'ensalada', 'patatas al horno', 'patatas a la francesa']

carne_elegida = random.choice(carnes)
sazonado_elegido = random.choice(sazonados)
guarnicion_elegida = random.choice(guarniciones)

print(f"Receta: {carne_elegida} a la {sazonado_elegido} con {guarnicion_elegida}")