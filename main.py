# main.py
# main.py: no es obligatorio ni afecta el funcionamiento del código, pero se pone por claridad y organización,
# Se suele poner al inicio del archivo principal del programa para que, si abrís muchos archivos al mismo tiempo en un editor (como VS Code o PyCharm), sea fácil identificar de qué archivo se trata sin mirar el nombre de la pestaña.

import json
from src.funciones import simular_rondas

def cargar_datos_rondas(ruta_archivo):
    """Carga el contenido de rounds.json desde la ruta especificada."""
    with open(ruta_archivo, 'r') as f:
        return json.load(f)

def mostrar_rondas(rounds):
    """Muestra los datos de cada ronda en formato legible."""
    for i, ronda in enumerate(rounds, 1):
        print(f"Ronda {i}:")
        for jugador, stats in ronda.items():
            print(f"  {jugador}: Kills={stats['kills']}, Assists={stats['assists']}, Deaths={stats['deaths']}")
        print("-" * 40)

# ______________________________________________________________________________________

ruta_archivo = 'data/rounds.json'
rounds = cargar_datos_rondas(ruta_archivo)
# mostrar_rondas(rounds)
simular_rondas(rounds)

#The SATO 😎