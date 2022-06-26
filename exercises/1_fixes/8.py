# Arregla el programa para mostrar únicamente los músculos de la pierna

def obtener_musculos(parte_del_cuerpo=None):
    brazo = ['biceps', 'triceps', 'deltoides', 'rotadores', 'redondo', 'flexores']
    pierna = ['cuadriceps', 'recto', 'tibial', 'vasto lateral', 'vasto medial', 'peroneo', 'sóleo']
    espalda = ['trapecio', 'redondo', 'dorsal', 'lumbar', 'romboide', 'infraespinoso']

    if parte_del_cuerpo:
        if parte_del_cuerpo == 'brazo':
            return brazo
        elif parte_del_cuerpo == 'pierna':
            return pierna
        elif parte_del_cuerpo == 'espalda':
            return espalda
        else:
            return 'No existe esa parte del cuerpo'
    else:
        cuerpo = brazo + pierna + espalda
        return cuerpo


musculos = obtener_musculos()
print(musculos)