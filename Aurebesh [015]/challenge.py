"""
DESCRIPTION:

/*
 * Crea una función que sea capaz de transformar Español al lenguaje básico
 * del universo Star Wars: el "Aurebesh".
 * - Puedes dejar sin transformar los caracteres que no existan en "Aurebesh".
 * - También tiene que ser capaz de traducir en sentido contrario.
 *
 * ¿Lo has conseguido? Nómbrame en twitter.com/mouredev y escríbeme algo en Aurebesh.
 *
 * ¡Que la fuerza os acompañe!
 */

""" 

def spanish_to_aurebesh(s:str) -> str:
    
    """
    Se encarga de traducir una cadena de texto en Español al 
    lenguaje ficticio Aurebesh.
    
    params:
        s (str)
    
    returns:
        str
    """
    
    # Diccionario de mapeo de caracteres
    aurebesh_dict = {
        'A': 'ꓮ', 'B': 'Ɓ', 'C': '☾', 'D': 'ꓷ', 'E': 'Ǝ', 'F': 'ꓝ', 'G': 'Ꮆ',
        'H': 'ꓧ', 'I': 'Ꙇ', 'J': 'ꓩ', 'K': 'ꓘ', 'L': 'ꓶ', 'M': 'ꓟ', 'N': 'И',
        'O': 'Ө', 'P': 'ꓑ', 'Q': 'Ǫ', 'R': 'ꓣ', 'S': 'Ϩ', 'T': 'ꓔ', 'U': 'Ա',
        'V': 'ꓦ', 'W': 'ꓪ', 'X': 'ꓫ', 'Y': 'Ƴ', 'Z': 'ꓜ',
        'a': 'ꭺ', 'b': 'ƀ', 'c': 'ɔ', 'd': 'ꝱ', 'e': 'ꬴ', 'f': 'ꬵ', 'g': 'ꬶ',
        'h': 'ɦ', 'i': 'ɨ', 'j': 'ꭻ', 'k': 'ꮶ', 'l': 'ꝉ', 'm': 'ɱ', 'n': 'ɲ',
        'o': 'ꭴ', 'p': 'ρ', 'q': 'ꝗ', 'r': 'ꭇ', 's': 'ʂ', 't': 'ꞇ', 'u': 'ꞟ',
        'v': 'ʋ', 'w': 'ꮙ', 'x': '×', 'y': 'ꭚ', 'z': 'ɀ',
        '0': '⓪', '1': '①', '2': '②', '3': '③', '4': '④', '5': '⑤',
        '6': '⑥', '7': '⑦', '8': '⑧', '9': '⑨'
    }
    
    # Diccionario de mapeo invertido.
    spanish_dict = {value:key for key, value in aurebesh_dict.items()}

    # Aurebesh no está disponible en Unicorde, por lo que utilizaremos caracteres 
    # visualmente parecidos a los de este lenguaje ficticio.
    
    # Evaluamos en qué idioma se encuentra la cadena recibida.
    spanish_chars = list(aurebesh_dict.keys())
    if any([True if (char in spanish_chars) else False for char in s]):
        # Creamos la cadena traduciendo los caracteres.
        translated_string = "".join([aurebesh_dict[char] if (char in aurebesh_dict) else char for char in s])
        return translated_string
    else:
        # Traducimos la cadena al español
        translated_string = "".join([spanish_dict[char] if (char in spanish_dict) else char for char in s])
        return translated_string


if __name__ == "__main__":
    
    # Probamos la función con una cadena de prueba
    example_string = "ꓟꞟꭚ ƀꞟꬴɲꭺʂ. Ǫꞟꬴ ꝉꭺ ꬵꞟꬴꭇɀꭺ ꭴʂ ꭺɔꭴɱρꭺñꬴ."
    translated_string = spanish_to_aurebesh(example_string)
    print(translated_string)