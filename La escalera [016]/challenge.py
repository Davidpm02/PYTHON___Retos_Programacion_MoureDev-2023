"""
DESCRIPTION:

/*
 * Crea una función que dibuje una escalera según su número de escalones.
 * - Si el número es positivo, será ascendente de izquiera a derecha.
 * - Si el número es negativo, será descendente de izquiera a derecha.
 * - Si el número es cero, se dibujarán dos guiones bajos (__).
 *
 * Ejemplo: 4
 *         _
 *       _|
 *     _|
 *   _|
 * _|
 *
 
"""

def make_stairs(step_stairs:int) -> str:
    
    """
    Se encarga de construir una escalera con tantos escalones
    como el valor del entero recibido como parámetro.
    
    Si el entero es positivo, las escaleras son ascendentes. Por
    otro lado, si el entero es negativo, serán descendentes.
    Si el entero es 0, la función retorna '__'.
    
    params:
        step_stairs (int)
    returns:
        str
    """
    
    if (step_stairs == 0):
        return ["__"]
    elif (step_stairs > 0):
        # Escaleras ascendentes
        stairs_start = " "*((step_stairs * 2) + 1) + "_"
        steps_list = [stairs_start]
        for i in range(step_stairs - 1, -1, -1):
            distance_to_left = ((i * 2) + 1)
            stairs_start = " " * distance_to_left + "_|"
            steps_list.append(stairs_start)
    else:
        # Escaleras descendentes
        stairs_start = "_"
        steps_list = [stairs_start]
        for i in range(abs(step_stairs)):
            distance_to_left = ((i * 2) + 1)
            stairs_start = " " * distance_to_left + "|_"
            steps_list.append(stairs_start)
    
    # for i in steps_list:
    #   print(i)
    
    return steps_list



if __name__ == "__main__":
    
    stairs = make_stairs(0)
    for stair in stairs:
        print(stair)