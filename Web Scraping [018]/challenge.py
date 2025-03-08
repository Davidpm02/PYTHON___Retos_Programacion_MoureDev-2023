"""
DESCRIPTION:

/*
 * El día 128 del año celebramos en la comunidad el "Hola Mundo day"
 * Vamos a hacer "web scraping" sobre su sitio web: https://holamundo.day
 *
 * Crea un programa que se conecte a la web del evento e imprima únicamente la agenda de eventos
 * del día 8. Mostrando hora e información de cada uno.
 * Ejemplo: "16:00 | Bienvenida"
 *
 * Se permite utilizar librerías que nos faciliten esta tarea.
 */
 
"""

import requests
from bs4 import BeautifulSoup

# URL del sitio web del "Hola Mundo Day"
URL = "https://holamundo.day"

# Ejecuto una petición GET
response = requests.get(URL)

# Parseando el contenido de la respuesta a la petición
text_response = response.text
content_response = BeautifulSoup(text_response, "html.parser")

# Obtengo el contenido de todas las etiquetas "div" del HTML
div_elements = content_response.find_all('div')

# Itero sobre los elementos 'div' y me quedo con aquel que contiene
# la información que me interesa
for div_element in div_elements:
    h2_tags = div_element.find_all('h2')  # Busco todos los <h2> dentro del <div>
        
    for h2 in h2_tags:
        if h2.text.strip() == 'Agenda':  # Comparo el texto eliminando espacios en blanco
            selected_div = div_element
            break  # Salgo del bucle interno si encuentro el elemento

print(div_element)
# Obtengo el contenido de la agenda marcada para el "Hola Mundo Day"
