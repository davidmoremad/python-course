# Arregla el programa para que tenga la lógica correcta
# El programa debe mostrar el mensaje "Bienvenido a la clinica. Pase a la sala de espera" para hora_actual = 14
# El programa debe mostrar el mensaje "Lo sentimos, la clinica esta cerrada" para hora_actual = 21

clinica_abierta = True
horario_entrada = 8 # 8 am
horario_salida = 20 # 8 pm

hora_actual = 24 # hora actual en el día

if clinica_abierta == True and horario_salida <= hora_actual and hora_actual <= horario_entrada:
    print("Bienvenido a la clinica. Pase a la sala de espera")
else:
    print("Lo sentimos, la clinica esta cerrada")