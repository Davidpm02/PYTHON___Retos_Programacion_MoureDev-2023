"""
DESCRIPTION:

/*
 * Crea un programa que analice texto y obtenga:
 * - Número total de palabras.
 * - Longitud media de las palabras.
 * - Número de oraciones del texto (cada vez que aparecen un punto).
 * - Encuentre la palabra más larga.
 *
 * Todo esto utilizando un único bucle.
 */

"""

from typing import Dict

def analize_text(text:str) -> Dict:
    
    # Inicializo un diccionario con claves cuyos parámetros
    # queremos contabilizar
    content_text_dict = {
        "words_in_text": 0,
        "median_length_of_words": 0,
        "length_of_sentences": [],
        "longest_word" : ""
    }
    length_of_words = []
    length_of_last_sentence = 0
    
    
    # Actualizo los valores del diccionario en un solo bucle
    for word in text.split(" "):
        
        length_of_words.append(len(word))
        length_of_last_sentence += 1
        content_text_dict["words_in_text"] += 1
        content_text_dict["median_length_of_words"] = sum(length_of_words) // len(length_of_words)
        
        if (len(content_text_dict["longest_word"]) < len(word)):
            content_text_dict["longest_word"] = word.replace('.', "")
        
        if (word.endswith('.')):
            content_text_dict["length_of_sentences"].append(length_of_last_sentence)
            length_of_last_sentence = 0
    
    return content_text_dict


if __name__ == "__main__":
    
    # Defino una párrafo de ejemplo
    text = "Hoy es sábado. Quiero ir al parque con mi hermana a jugar a los columpios."
    content_text_dict = analize_text(text=text)
    
    # Muestro la info obtenido del texto
    for key, value in content_text_dict.items():
        if (key == "words_in_text"):
            print('Número de palabras en el texto: -->', content_text_dict[key], ".")
        elif (key == "median_length_of_words"):
            print('Longitud media de las palabras en el texto -->', content_text_dict[key], ".")
        elif (key == "length_of_sentences"):
            print('Longitud de las oraciones del texto -->', content_text_dict[key], ".")
        elif (key == "longest_word"):
            print('Palabra más larga del texto -->', content_text_dict[key], ".")
        
        