"""
DESCRIPTION:

/*
 * Crea 3 funciones, cada una encargada de detectar si una cadena de
 * texto es un heterograma, un isograma o un pangrama.
 * - Debes buscar la definición de cada uno de estos términos.
 */
"""

# IMPORTS -----
from collections import Counter

def is_heterogram(s:str) -> bool:
    """
    Se encarga de comprobar si la cadena recibida es un
    heterograma o no.
    
    Según su definición, un heterograma es una palabra o 
    frase que no contiene ninguna letra repetida.
    
    params:
        s (str)
    
    returns:
        bool
    """
    
    # Elimino los espacios de la cadena
    s = s.replace(" ", "")
    
    try:
        chars_counter = Counter(s)
        assert all((value == 1) for value in list(chars_counter.values()))
        return True
    except AssertionError:
        return False



def is_isogram(s:str) -> bool:
    """
    Se encarga de comprobar si la cadena recibida es un
    isograma o no.
    
    Según su definición, un isograma es una palabra sin
    repetición de letras (como ambidiestro) o, más ampliamente,
    una palabra en la que las letras aparecen el mismo número de veces.
    
    params:
        s (str)
    
    returns:
        bool
    """
    
    # Elimino los espacios de la cadena
    s = s.replace(" ", "")
    
    try:
        chars_counter = Counter(s)
        
        # Tomo como referencia el número de repeticiones del primer carácter
        maximum_reps = list(chars_counter.values())[0]
        assert all((value == maximum_reps) for value in list(chars_counter.values()))
        return True
    except AssertionError:
        return False



def is_pangram(s:str) -> bool:
    """
    Se encarga de comprobar si la cadena recibida es un
    pangrama o no.
    
    Según su definición, un pangrama es una oración o frase
    que incluye todas las letras del alfabeto al menos una vez.
    
    params:
        s (str)
    
    returns:
        bool
    """
    
    # Elimino los espacios de la cadena
    s = s.replace(" ", "")
    
    # Lista con las letras del alfabeto
    abc_list = [chr(i) for i in range(ord('a'), ord('z') + 1)] + ['ñ']
    reps_list = [0 for i in range(len(abc_list))]
    
    # Mapeo las letras con cada número de repeticiones
    chars_counter = dict(zip(abc_list, reps_list))
    
    try:
        # Actualizo el contador de cada letra en chars_counter
        for char in s:
            chars_counter[char] +=1
        assert (0 not in list(chars_counter.values()))
        return True
    except AssertionError:
        return False