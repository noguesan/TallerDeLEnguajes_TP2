def crear_diccionario_puntos():
    """
    Devuelve un diccionario que asigna puntos a cada acción.
    """
    return {
        'kill': 3,
        'assist': 1,
        'death': -1
    }

def crear_diccionario_estadisticas(jugadores):
    """
    Inicializa un diccionario con las estadísticas de cada jugador en cero.
    """
    return {
        jugador: {'kills': 0, 'assists': 0, 'deaths': 0, 'mvp': 0, 'points': 0}
        for jugador in jugadores
    }

def copiar_diccionario_con_ceros(diccionario_original):
    """
    Crea una copia del diccionario con todas las estadísticas puestas a cero.
    """
    copia = {}
    for clave, subdic in diccionario_original.items():
        copia[clave] = {k: 0 for k in subdic}
    return copia

# Función para calcular el puntaje y actualizar las estadísticas
def actualizar_estadisticas(round_data, estadisticas_jugadores, points):
    """
    Calcula los puntajes de una ronda, actualiza las estadísticas acumuladas
    y determina el MVP de la ronda.
    round_data: informacion de las rondas
    estadisticas_jugadores: diccionario con las estadisticas de cada jugador
    points: diccionario con los puntos asignados a cada accion
    """
    mvp = None
    max_puntos_ronda = float('-inf')  # Inicializamos con un valor muy bajo

    # Diccionario temporal para almacenar los valores de la ronda
    ronda_stats = copiar_diccionario_con_ceros(estadisticas_jugadores)

    for jugador, stats in round_data.items():
        kills = stats['kills'] # carga para jugador el stats correspondinte a kills de la ronda_data
        assists = stats['assists']
        deaths = stats['deaths']

        # Calcular puntos de la ronda
        puntos_ronda = kills * points['kill'] + assists * points['assist'] + (points['death'] if deaths else 0)

        # Guardar estadísticas de la ronda en el diccionario temporal
        ronda_stats[jugador]['kills'] = kills
        ronda_stats[jugador]['assists'] = assists
        ronda_stats[jugador]['deaths'] = 1 if deaths else 0
        ronda_stats[jugador]['points'] = puntos_ronda

        # Identificar al MVP de la ronda
        if mvp is None or puntos_ronda > max_puntos_ronda:
            mvp = jugador
            max_puntos_ronda = puntos_ronda  # Actualizamos el máximo de la ronda

    # Actualizar MVP
    if mvp:
        ronda_stats[mvp]['mvp'] += 1
    
    # Mostrar ranking de la ronda antes de actualizar los valores acumulados
    mostrar_ranking(ronda_stats, f"Estadísticas de la ronda (MVP: {mvp})")

    # Actualizar estadísticas generales
    for jugador in estadisticas_jugadores:
        estadisticas_jugadores[jugador]['kills'] += ronda_stats[jugador]['kills']
        estadisticas_jugadores[jugador]['assists'] += ronda_stats[jugador]['assists']
        estadisticas_jugadores[jugador]['deaths'] += ronda_stats[jugador]['deaths']
        estadisticas_jugadores[jugador]['points'] += ronda_stats[jugador]['points']
        estadisticas_jugadores[jugador]['mvp'] += ronda_stats[jugador]['mvp']

    # Mostrar ranking con los valores acumulados actualizados
    mostrar_ranking(estadisticas_jugadores, f"Estadísticas actualizadas")

    return mvp

# Función para mostrar el ranking de la ronda o total
def mostrar_ranking(stats, titulo="Ranking total"):
    """
    Muestra un ranking ordenado por puntos, con todas las estadísticas.
    """  
    ranking = sorted(stats.items(), key=lambda x: x[1]['points'], reverse=True) # x[1] accede al diccionario de jugadores
    # """
    # notas de la parte del codigo x[1]['points']
    # dict_items([
    # ('Shadow', {'kills': 5, 'assists': 3, 'deaths': 2, 'mvp': 1, 'points': 16}),
    # ('Blaze', {'kills': 7, 'assists': 2, 'deaths': 3, 'mvp': 0, 'points': 20}),
    # ('Viper', {'kills': 4, 'assists': 5, 'deaths': 1, 'mvp': 2, 'points': 18})
    # ])
    # Cada elemento es una tupla donde:

    # x[0] es el nombre del jugador (Ejemplo: "Shadow")

    # x[1] es su diccionario de estadísticas
    # (Ejemplo: {'kills': 5, 'assists': 3, 'deaths': 2, 'mvp': 1, 'points': 16})

    # """

    print(f"\n{titulo}")
    print(f"{'Jugador':<10} {'Kills':<6} {'Asistencias':<12} {'Muertes':<8} {'Puntos':<8} {'MVP':<6}")
    # :<10 -->  se alinea a la izquierda (<) y ocupa 10 espacios.
    print("-" * 60)
    for jugador, stat in ranking:
        mvp_value = stat['mvp'] if 'mvp' in stat else '-'  # Usamos '-' si no tiene mvp
        print(f"{jugador:<10} {stat['kills']:<6} {stat['assists']:<12} {stat['deaths']:<8} {stat['points']:<8} {mvp_value:<6}")
    print("-" * 60)

def simular_rondas(rounds):
    """
    Ejecuta la simulación de todas las rondas y muestra los resultados.
    """
    jugadores = list(rounds[0].keys())
    points = crear_diccionario_puntos()
    estadisticas_jugadores = crear_diccionario_estadisticas(jugadores)

    for round_num, round_data in enumerate(rounds, 1):
        # round_num recibe el número de la ronda (1, 2, 3, …).
        # round_data recibe el diccionario con las estadísticas de los jugadores en esa ronda.
        print(f"\nRonda {round_num}:")
        actualizar_estadisticas(round_data, estadisticas_jugadores, points)
        print("_" * 100)