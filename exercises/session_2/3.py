# Este script muestra los eventos de Madrid. No funciona porque le falta una linea.
# Aunque hay cosas que no entendéis, el error es fácil de ver. Es algo que hemos visto
# y para detectarlo habrá que leer el programa entero.
# Este ejercicio es difícil porque requiere leer mucho y entender lo que hace cada función,
# pero es muy útil para aprender a leer código de otros. Puedes tomar notas para recordar lo que hace cada cosa o hacerte un diagrama.

import requests

api_endpoint = 'https://datos.madrid.es/egob/catalogo/206974-0-agenda-eventos-culturales-100.json'

def request_url(url):
    # Hace peticion web a la url dada
    response = requests.get(url)

def request_madrid_events():
    # Hace petición web a la API de eventos de Madrid
    eventos = request_url(api_endpoint)
    return eventos.json()['@graph']

def print_event_format(event):
    # Imprime el evento en formato legible
    title = event["title"][:70].ljust(70)
    fecha = event["dtstart"][:10]
    lugar = event["event-location"][:50].ljust(50)
    print(f'{fecha} - {title} \t {lugar}')

def main():
    # 1. Obtener eventos de Madrid
    events = request_madrid_events()

    # 2. Ordenar eventos por fecha
    events = sorted(events, key=lambda d: d['dtstart'])

    # 3. Mostrar eventos ordenados
    for event in events:
        print_event_format(event)

main()