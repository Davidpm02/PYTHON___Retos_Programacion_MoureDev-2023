"""
DESCRIPTION:

/*
 * Dada una URL con parámetros, crea una función que obtenga sus valores.
 * No se pueden usar operaciones del lenguaje que realicen esta tarea directamente.
 *
 * Ejemplo: En la url https://retosdeprogramacion.com?year=2023&challenge=0
 * los parámetros serían ["2023", "0"]
 */
"""

## IMPORTS -----
from urllib.parse import urlparse
from typing import List

def get_url_params(url:str) -> List[str]:
    
    """
    Parsea una URL dada y retorna una lista con todos los
    parámetros que esta contenga.
    
    params:
        url (str) -- URL a pasear.
    returns:
        List[str] -- Lista con todos los parámetros enviados 
        a la URL. 
        En caso de que la URL no contenga parámetro, se devolverá
        una lista vacía.
    """
    
    parse_result = urlparse(url)
    
    # Accedo a los parámetros enviados a la URL
    url_query = parse_result[4]
    components_url_query = url_query.split("&")
    url_params = [param.split("=")[-1] for param in components_url_query]
    
    return url_params
    
    