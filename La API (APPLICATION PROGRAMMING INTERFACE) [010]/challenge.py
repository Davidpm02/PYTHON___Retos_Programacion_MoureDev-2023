"""
DESCRIPTION:

/*
 * Llamar a una API es una de las tareas más comunes en programación.
 *
 * Implementa una llamada HTTP a una API (la que tú quieras) y muestra su
 * resultado a través de la terminal. Por ejemplo: Pokémon, Marvel...
 *
 * Aquí tienes un listado de posibles APIs:
 * https://github.com/public-apis/public-apis
 */
"""

## IMPORTS -----
import urllib.request


## FUNCTIONS -----

def get_superhero_namelist():
    
    """
    Obtiene un listado con los nombres de superheroes que 
    coinciden con el nombre proporcionado por el usuario,
    e imprime el resultado por pantalla.
    
    params:
    
    returns:
    
    """
    
    ref_name = input('Por favor, escribe el nombre del superheroe:')
    url_api = f"https://superheroapi.com/api/a6e554363e55bbc08b8e995ac29d5872/search/{ref_name}"

    # La API retorna un objeto con la respuesta
    api_response = dict(urllib.request.urlopen(url_api))
    superhero_namelist = []
    for result in api_response['results']:
        superhero_namelist.append(result['name'])
    
    print('Los superheroes coincidentes con el nombre proporcionado son:', end="\n")
    for superhero_name in superhero_namelist:
        print("  -", superhero_name, end='\n')