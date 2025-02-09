"""
DESCRIPTION:

/*
 * Crea una función que reciba un número decimal y lo trasforme a Octal
 * y Hexadecimal.
 * - No está permitido usar funciones propias del lenguaje de programación que
 * realicen esas operaciones directamente.
 */

"""

# IMPORTS -----
import copy

# FUNCTIONS -----

def decimal_to_octal_n_hexadecimal(num:int) -> tuple[int, str]:
    
    """
    Se encarga de convertir un entero en sistema decimal a sus
    correspondiente versiones en sistemas octal y hexadecimal.
    
    params:
        num (int)
    
    returns:
        tuple[int, str]
    """
    
    # Verificamos que el entero recibido sea distinto de cero
    if (num == 0):
        return (0, "0")
    
    # Aplicamos el procedimiento de conversión a octal
    number = copy.copy(num)
    rest_list = []  # Restos de las divisiones
    while (number != 0):
        
        # Dividimos entre 8 hasta que ya no sea posible
        rest_list.append(str(number % 8))
        number = number // 8
    
    octal_num = int("".join(rest_list[::-1]))
    
    
    
    # Aplicamos el procedimiento de conversión a hexadecimal
    hex_chars = "0123456789ABCDEF"  # Mapeo de valores hexadecimales
    number = copy.copy(num)
    hex_num = ""
    while (number != 0):
        
        # Dividimos entre 16 hasta que ya no sea posible
        rest = number % 16
        hex_num = f"{hex_chars[rest]}" + hex_num
        number = number // 16
    
    # Retonamos los resultados
    return (octal_num, hex_num)


if __name__ == "__main__":

    octal_value, hex_value = decimal_to_octal_n_hexadecimal(345)     
    print(octal_value, hex_value)
        