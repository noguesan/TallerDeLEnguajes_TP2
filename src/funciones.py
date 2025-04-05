# Funciones y variables

# _________________________________________________________________________________________________________
# VARIABLES

# valores para cada tipo de estadistica
points = {
    'kill': 3,
    'assist': 1,
    'death': -1
}

# _________________________________________________________________________________________________________

# FUNCIONES
# Función para calcular el puntaje y actualizar las estadísticas
def actualizar_estadisticas(round_data):
    """
    Procesa los datos de una ronda específica, calcula los puntos obtenidos por cada jugador
    y actualiza sus estadísticas acumuladas (kills, assists, deaths, puntos y MVP).

    También identifica al jugador con mayor puntaje de la ronda (MVP),
    muestra el ranking de esa ronda y luego actualiza el ranking acumulado.

    Parámetros:
        round_data (dict): Diccionario con las estadísticas de cada jugador en una ronda,
        incluyendo kills, assists y si murió o no.
        ejemplo:
        round_data = {
                    'Shadow': {'kills': 2, 'assists': 1, 'deaths': True},
                    'Blaze': {'kills': 1, 'assists': 0, 'deaths': False},
                    'Viper': {'kills': 1, 'assists': 2, 'deaths': True},
                    'Frost': {'kills': 0, 'assists': 1, 'deaths': False},
                    'Reaper': {'kills': 1, 'assists': 1, 'deaths': False}
                    }

    Retorna:
        str: Nombre del jugador que fue MVP en la ronda.
    """

    mvp = None
    max_puntos_ronda = float('-inf')  # Inicializamos con un valor muy bajo

    # Diccionario temporal para almacenar los valores de la ronda
    ronda_stats = {jugador: {'kills': 0, 'assists': 0, 'deaths': 0, 'points': 0} for jugador in jugadores}

    for jugador, stats in round_data.items():
        kills = stats['kills']
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

    # Mostrar ranking de la ronda antes de actualizar los valores acumulados
    mostrar_ranking(ronda_stats, f"Estadísticas de la ronda (MVP: {mvp})")

    # Actualizar estadísticas generales
    for jugador in jugadores:
        jugadores[jugador]['kills'] += ronda_stats[jugador]['kills']
        jugadores[jugador]['assists'] += ronda_stats[jugador]['assists']
        jugadores[jugador]['deaths'] += ronda_stats[jugador]['deaths']
        jugadores[jugador]['points'] += ronda_stats[jugador]['points']

    # Mostrar ranking con los valores acumulados actualizados
    mostrar_ranking(jugadores, f"Estadísticas actualizadas")

    # Actualizar MVP
    if mvp:
        jugadores[mvp]['mvp'] += 1

    return mvp

# _________________________________________________________________________________________________________

# Función para mostrar el ranking de la ronda o total
def mostrar_ranking(stats, titulo="Ranking total"):
    """
    Muestra un ranking ordenado de los jugadores según los puntos obtenidos,
    ya sea en una ronda específica o acumulados.

    El ranking se presenta en una tabla con columnas de kills, asistencias,
    muertes y puntos.

    Parámetros:
        stats (dict): Diccionario con las estadísticas de los jugadores.
        titulo (str): Título que se mostrará arriba del ranking (opcional).
        ejemplo:
            stats_de_ejemplo = {
                                'Shadow': {'kills': 4, 'assists': 3, 'deaths': 2, 'points': 13},
                                'Blaze': {'kills': 5, 'assists': 1, 'deaths': 1, 'points': 15},
                                'Viper': {'kills': 2, 'assists': 4, 'deaths': 0, 'points': 10}
                                }

            titulo = "Ranking de prueba (Ronda 1)"
    """
    ranking = sorted(stats.items(), key=lambda x: x[1]['points'], reverse=True) # x[1] accede al diccionario de jugadores

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

    print(f"\n{titulo}")
    print(f"{'Jugador':<10} {'Kills':<6} {'Asistencias':<12} {'Muertes':<8} {'Puntos':<6}")
    # :<10 -->  se alinea a la izquierda (<) y ocupa 10 espacios.
    print("-" * 50)
    for jugador, stat in ranking:
        print(f"{jugador:<10} {stat['kills']:<6} {stat['assists']:<12} {stat['deaths']:<8} {stat['points']:<6}")
    print("-" * 50)


