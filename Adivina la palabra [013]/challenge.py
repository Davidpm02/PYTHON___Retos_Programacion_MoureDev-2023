"""
DESCRIPTION:

/*
 * Crea un pequeño juego que consista en adivinar palabras en un número máximo de intentos:
 * - El juego comienza proponiendo una palabra aleatoria incompleta
 *   - Por ejemplo "m_ur_d_v", y el número de intentos que le quedan
 * - El usuario puede introducir únicamente una letra o una palabra (de la misma longitud que
 *   la palabra a adivinar)
 *   - Si escribe una letra y acierta, se muestra esa letra en la palabra. Si falla, se resta
 *     uno al número de intentos
 *   - Si escribe una resolución y acierta, finaliza el juego, en caso contrario, se resta uno
 *     al número de intentos
 *   - Si el contador de intentos llega a 0, el jugador pierde
 * - La palabra debe ocultar de forma aleatoria letras, y nunca puede comenzar
 *   ocultando más del 60%
 * - Puedes utilizar las palabras que quieras y el número de intentos que consideres
 */
 
"""

# IMPORTS -----
import random
from typing import List, Dict


# FUNCTIONS -----

def generate_random_word() -> str:
    
    # Lista finita de palabras
    available_words = ['dinosaurio', 'cebolla', 'programa', 'ordenador', 'pikachu', 'entrenamiento', 'machine', 'mouredev', 'charmander']
    random_word = random.choice(available_words)
    return random_word


def update_counter(tries_counter:int) -> int:
    
    tries_counter -= 1
    return tries_counter

def solving_word(original_word:str, word:str, idx_to_char:Dict, selected_letters:List[str]):
    pass

def show_word_and_counter(word:str, counter_tries:int):
    
    print(f'PALABRA ESCOGIDA: {word}   ----   Intentos restantes: {counter_tries}')

def select_random_blanks_word(word:str):
    
    # Defino una lista con los caracteres de la cadena.
    chars_in_word = [char for char in word]
    
    # Número de caracteres en la cadena.
    n_chars = len(chars_in_word)
    
    # Calculo el 60% del total de caracteres, y escojo un 
    # número aleatorio de caracteres ocultos.
    max_hidden_chars = n_chars * 0.6
    hidden_chars = random.randint(1, max_hidden_chars)
    
    # Selecciono aleatoriamente los caracteres a eliminar
    idx_chars_in_word = [idx for idx, char in enumerate(chars_in_word)]
    idx_chars_to_hidden = random.sample(idx_chars_in_word, hidden_chars)
    
    # Defino un diccionario que mapee los indices escogidos con sus
    # correspondientes caracteres
    idx_to_char = {idx: chars_in_word[idx] for idx in idx_chars_to_hidden}
    return idx_to_char


def match_character(selected_char:str, hidden_chars:List[str]) -> bool:
    
    if (selected_char in hidden_chars):
        hidden_chars.remove(selected_char)
        return True
    return False


if __name__ == "__main__":
    
    print('¡Bienvenido al juego "Adivina la palabra"!')
    user_input = input('Presiona cualquier tecla para comenzar.')
    if user_input:
        
        # Defino una variable inicial de referencia al estado de la partida
        player_has_won = False
        
        # Escogemos la palabra aleatoria
        random_word = generate_random_word()
        remaining_tries = 5 # 5 intentos por defecto
        
        # Oculto los caracteres de la palabra escogida
        idx_to_char = select_random_blanks_word(word=random_word)
        word_to_solve, remaining_chars, hidden_chars = solving_word(original_word=random_word,
                                                                    word=word_to_solve,
                                                                    idx_to_char=idx_to_char,
                                                                    selected_letters=[])
        
        # Bucle de resolución del juego
        while (remaining_tries > 0):
            show_word_and_counter(word=word_to_solve,
                                  counter_tries=remaining_tries)
            selected_char = input('Selecciona una letra:')
            if match_character(selected_char, hidden_chars):
                word_to_solve, remaining_chars, hidden_chars = solving_word()
                if (remaining_chars == 0):
                    player_has_won = True
                    break
            else:
                remaining_tries = update_counter(remaining_tries)
        if (player_has_won == True):
            print(f'¡Enhorabuena! La palabra escogida era: "{random_word}".')
        else:
            print(f'¡Oh! No has conseguido adivinar la palabra. ¡Mucha suerte en tu próximo intento!')