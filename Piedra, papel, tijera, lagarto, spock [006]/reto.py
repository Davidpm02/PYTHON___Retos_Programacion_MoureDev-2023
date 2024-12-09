"""
/*
 * Crea un programa que calcule quien gana más partidas al piedra,
 * papel, tijera, lagarto, spock.
 * - El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
 * - La función recibe un listado que contiene pares, representando cada jugada.
 * - El par puede contener combinaciones de "🗿" (piedra), "📄" (papel),
 *   "✂️" (tijera), "🦎" (lagarto) o "🖖" (spock).
 * - Ejemplo. Entrada: [("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")]. Resultado: "Player 2".
 * - Debes buscar información sobre cómo se juega con estas 5 posibilidades.
 */
 
"""

# Este archivo contiene un script que se encarga de procesar una entrada, dada en forma de lista,
# que contiene una secuencia de jugadas al Piedra,Papel,Tijera,Lagarto,Spock.
# Cada elemento de esta secuencia de jugadas contiene otros 2 elementos, y cada uno de
# estos representa la jugada de un jugador en concreto (max. 2 jugadores posibles).

# A continuacion, se muestra la forma en la que se juega a este juego:

"""
Las tijeras cortan el papel.
El papel cubre la piedra.
La piedra aplasta el lagarto.
El lagarto envenena a Spock.
Spock aplasta las tijeras.
Las tijeras decapitan el lagarto.
El lagarto se come el papel.
El papel refuta a Spock.
Spock vaporiza la piedra.
La piedra aplasta a las tijeras.
"""


def retornarGanador(resultado_jugador1, resultado_jugador2):
    
    """Funcion parametrizada encargada de leer una secuencia recibida como parametro
       y retornar un resultado acorde a ella.
       
       Args:
          - dict_resultado_secuencia ==> diccinario con los resultados de la partida entre
                                         Jugador 1 y Jugador 2.
       
       Returns:
          - resultado ==> literal que contiene una cadena con el nombre del jugador
                          que ha ganado la mayoria de partidas dentro de la secuencia recibida
                          como parametro de la funcion.
    """
    
    if resultado_jugador1 > resultado_jugador2:
        match_winner = "Player 1"
    elif resultado_jugador1 < resultado_jugador2:
        match_winner = "Player 2"
    else:  # Si ninguno de los resultados es mayor o menor, es porque son iguales (EMPATE)
        match_winner = "Tie"
        
    return match_winner


def generarDictMatch():
    
    """Funcion sin parametros que se encarga de generar y retornar un diccionario con el valor
       que contiene cada uno de los valores para los jugadas de los usuarios.
       
       Args:
       
       Returns:
          - dict_jugadas ==> diccionario cuyos pares clave: valor es similar a ["📄": "papel"].
                             Esto nos permite mapear cada una de las jugadas posibles.
    """
    
    valid_games = ["🗿", "📄", "✂️", "🦎", "🖖"]
    valid_games_names = ["piedra", "papel", "tijera", "lagarto", "spock"]
    
    dict_valid_games = dict(zip(valid_games, valid_games_names)) # Hashmap que mapea cada una de las jugadas posibles
    
    return dict_valid_games


def encontrarGanadorJugada(secuencia_partidas, dict_valid_games):
    
    """Funcion parametrizada que se encarga de procesar la secuencia de jugadas llevadas a cabo entre dos
       jugadores al juego, y devolver una variables contador con el resultado obtenido de la secuencia de jugadas.
       
       Args:
          - secuencia_partidas ==> lista de jugadas llevadas a cabo por 2 jugadores al juego
                                   Piedra,Papel,Tijera,Lagarto,Spock.
          - dict_valid_games ==> diccionario que mapea cada una de las acciones posibles en el juego que
                                 se lleva a cabo.
    
       Returns:
          - resultado_jugador1 ==> contador con las veces que el Jugador 1 ha ganado.
          - resultado_jugador2 ==> contador con als veces que el Jugador 2 ha ganado.
    """
    
    # Teniendo en cuenta la forma de jugar a este juego, defino las jugadas posibles.
    # Comienzo creando un diccionario de debilidades para cada una de las posibles jugadas.
    
    dict_debilidades = {
        "piedra": ["papel", "spock"],
        "papel": ["tijera", "spock"],
        "tijera": ["spock", "piedra"],
        "lagarto": ["piedra", "tijera"],
        "spock": ["lagarto", "papel"]
    }
    
    # Defino las variable contador que sumaran las victorias de cada jugador
    resultado_jugador1 = 0
    resultado_jugador2 = 0
    
    
    
    
    # Ahora itero sobre las jugadas que conforman la secuencia de partidas de los jugadores
    # Defino una lista con las debilidades de la eleccion del Jugador 1
    player1_weaks = []
    action_player1 = ""
    
    
    for game in secuencia_partidas:
        for indice, posibility in enumerate(game):
                        
            if indice == 1:
                # Si estamos iterando sobre la accion del Jugador 2 en una jugada...
                posibility_name = dict_valid_games[posibility]
                
                if posibility_name == action_player1:
                    pass
                elif posibility_name in player1_weaks:
                    resultado_jugador2 +=1
                elif posibility_name not in player1_weaks:
                    resultado_jugador1 +=1
                
            else:
    
                posibility_name = dict_valid_games[posibility]
                action_player1 = posibility_name
                
                # Ahora tengo el nombre de la jugada del jugador 1. Busco sus debilidades.
                player1_weaks = dict_debilidades[posibility_name]
        
    else: # Cuando recorro todo el contenido de la secuencia recibida como parametro
        return resultado_jugador1, resultado_jugador2
    

if __name__ == "__main__":
    
    secuencia_partidas = [("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")]
    
    dictMatch = generarDictMatch()
    
    # Invoco a la funcion encontrarGanadorJugada(), encargada de procesar la secuencia de partidas, y devolver la puntuacion para cada
    # uno de los jugadores.
    result_Player1, result_Player2 = encontrarGanadorJugada(secuencia_partidas, dictMatch)
    
    match_winner = retornarGanador(result_Player1, result_Player2)
    
    # Muestro por pantalla el jugador que ha obtenido mas puntos en la secuencia de partidas.
    print(match_winner)