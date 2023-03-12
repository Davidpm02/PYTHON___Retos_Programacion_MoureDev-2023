#/*
 #* Escribe un programa que reciba un texto y transforme lenguaje natural a
 #* "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 #*  se caracteriza por sustituir caracteres alfanuméricos.
 #* - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
 #*   con el alfabeto y los números en "leet".
 #*   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
#*/


def convertirTextoLeet(texto):
    """Función parametrizada que se encarga de recibir texto proporcionado por el usuario y devolver su correspondiente traducción
       al lenguaje Leet.
       Mi función solo va a contemplar la opción más común de traducción para cada letra/número de la cadena 'texto'.
       
       Parametros:
           - texto: string en lenguaje natural que utiliza la función para hallar su traducción al lenguaje Leet.
    """
    
    textoNormalizado = texto.lower()  # Normalizo el argumento recibido a minusculas.
   
 
    numeros = [0,1,2,3,4,5,6,7,8,9]
    letras = ['abcdefghijklmnopqrstuvwxyz']
    
    
    listaPalabrasTexto = textoNormalizado.split()
    

    
    
    
    for palabra in listaPalabrasTexto:
        palabras = []
        for letra in palabra:
            if letra in letras:
                if letra == 'a':
                    palabras.append('4')
                elif letra == 'b':
                    palabras.append('I3')
                elif letra == 'c':
                    palabras.append('[')
                elif letra == 'd':
                    palabras.append('I>')
                elif letra == 'e':
                    palabras.append('3')
                elif letra == 'f':
                    palabras.append('|=')
                elif letra == 'g':
                    palabras.append('&')
                elif letra == 'h':
                    palabras.append('#')
                elif letra == 'i':
                    palabras.append('1')
                elif letra == 'j':
                    palabras.append(',_|')
                elif letra == 'k':
                    palabras.append('>|')
                elif letra == 'l':
                    palabras.append('£')
                elif letra == 'm':
                    palabras.append('JVI')
                elif letra == 'n':
                    palabras.append('^/')
                elif letra == 'o':
                    palabras.append('0')
                elif letra == 'p':
                    palabras.append('|*')
                elif letra == 'q':
                    palabras.append('9')
                elif letra == 'r':
                    palabras.append('I2')
                elif letra == 's':
                    palabras.append('5')
                elif letra == 't':
                    palabras.append('7')
                elif letra == 'u':
                    palabras.append('v')
                elif letra == 'v':
                    palabras.append('\/')
                elif letra == 'w':
                    palabras.append('VV')
                elif letra == 'x':
                    palabras.append('><')
                elif letra == 'y':
                    palabras.append('j')
                elif letra == 'z':
                    palabras.append('7_')
            elif letra in numeros:
                if letra == 0:
                    palabras.append('o')
                elif letra == 1:
                    palabras.append('L')
                elif letra == 2:
                    palabras.append('R')
                elif letra == 3:
                    palabras.append('E')
                elif letra == 4:
                    palabras.append('A')
                elif letra == 5:
                    palabras.append('S')
                elif letra == 6:
                    palabras.append('b')
                elif letra == 7:
                    palabras.append('T')
                elif letra == 8:
                    palabras.append('B')
                elif letra == 9:
                    palabras.append('g')
        else:  # Este bloque se ejecutara tras procesar cada palabra del texto del usuario.
        
            listaPalabrasTraducidas = ''.join(palabras)
            del palabras
            
            
    textoFinal = ' '.join(listaPalabrasTraducidas)
    return textoFinal  
    
            
   




def traductorLEET():
    texto = input('Escribe el texto que deseas convertir en "lenguaje Hacker":')
    
    textoTraducido = convertirTextoLeet(texto)
    print(textoTraducido)
    return textoTraducido


if __name__ == '__main__':
    
    texto = traductorLEET()
    print(texto)