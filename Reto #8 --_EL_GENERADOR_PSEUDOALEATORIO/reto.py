"""
/*
 * Crea un generador de números pseudoaleatorios entre 0 y 100.
 * - No puedes usar ninguna función "random" (o semejante) del
 *   lenguaje de programación seleccionado.
 *
 * Es más complicado de lo que parece...
 */
"""


# Como todos los retos de programacion de este estilo, lo resolvere haciendo uso de Python
# Para escoger el numero elegido, me basare en otros numeros.
# Por ejemplo, voy ha hacer uso de los milisegundos de la hora real al momento de ejecucion del script


import time

# Defino una funcion que me permita procesar la hora en milisegundos

def process_miliseconds():
    
    
    while True:
        actual_mls = time.time()*1000.0
        actual_mls_str = str(actual_mls)
        
        # Utilizo la hora en milisegundos actual para quedarme con los 3 ultimos digitos:
        pseudorandom_value = actual_mls_str[-3:]
        
        # Ahora, proceso este valor, que puede estar comprendido entre 000 y 999
        # Se procesa todo el valor, en caso de que este contenga una coma
        pseudorandom_value = pseudorandom_value.lstrip(".")
        if int(pseudorandom_value) > 100:
            continue
        else:
            if int(pseudorandom_value) < 100:
                pseudorandom_value = pseudorandom_value.lstrip(".,0")
                return pseudorandom_value
            elif pseudorandom_value == "000":
                return 0
            else:
                return pseudorandom_value


pseudorandom_value = process_miliseconds()
print("PSEUDORANDOM VALUE GENERATED: {}".format(pseudorandom_value))
