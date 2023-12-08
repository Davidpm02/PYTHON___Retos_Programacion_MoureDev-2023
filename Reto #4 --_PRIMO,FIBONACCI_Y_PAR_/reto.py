"""
/*
 * Escribe un programa que, dado un número, compruebe y muestre si es primo,
 * fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
 */
 
"""

# Este script contiene codigo necesario para hallar una solucion efectiva al problema que se describe en el texto anterior.
# Se plantean definir una serie de funciones auxiliares que permitan actuar como filtro recibiendo un booleano que determine la condicion del numero escrito por el usuario


def es_primo(numero_usuario):
    
   """Funcion parametrizada que se encarga de procesar un numero recibido como argumento, y verificar que se trate de un numero primo.
    
       Args:
          - numero_usuario ==> entero proporcionado por el usuario por teclado.
       
       Returns:
          - boolean ==> booleano que determina si el parametro de la funcion cumple o no la condicion descrita.
   """
    
   # INFO. Un numero primo es aquel que es divisible por 1 y por si mismo (y por ningun otro numero real mas que sea inferior a este)
    
   try:
      # Creo una lista de numeros comprendidos entre 1 y el numero proporcionado por el usuario
      lista_numeros = list(range(1, numero_usuario))
      
      # Creo otra lista con los numeros que deben ser divisibles
      lista_validos = [1, numero_usuario]
      
      # Ahora debo asegurarme que los valores de "lista_validos" no se incluyen dentro de "lista_numeros"
      for valido in lista_validos:
         if valido in lista_numeros:
            lista_numeros.remove(valido)
            
      
      divisibles_encontrados = []  # Para ser primo, la lista deberia seguir vacia al finalizar el bucle for de abajo
      
      for numero in lista_numeros:
         if numero_usuario % numero == 0:
            divisibles_encontrados.append(numero)
            
      unicos_divisibles = []
      
      for valido in lista_validos:
         
         # Realizo la misma comprobacion, a pesar de que un numero siempre es divisible entre 1 y el mismo
         if numero_usuario % valido == 0:
            unicos_divisibles.append(valido)
            
            
      # Retorno el resultado de la funcion
      if len(divisibles_encontrados) == 0 and len(unicos_divisibles) == 2:
         return True
      else:
         return False

   except Exception as e:
      print("Ha ocurrido un error al revisar si el numero proporcionado por el usuario es un numero primo ==> ", e)

# -------------------------------------------------------------------


def pertenece_sucFibonacci(numero_usuario):
    
   """Funcion parametrizada que se encarga de procesar un numero proporcionado por el usuario, y confirmar si pertenece o no a la sucesion de Fibonacci.
    
      Args:
        - numero_usuario ==> entero proporcionado por el usuario por teclado.
        
      Returns:
        - boolean ==> booleano que determina si el parametro de la funcion cumple o no la condicion descrita.
   """
     
   # INFO. La sucesion de Fibonacci es una sucesion matematica que se rige por las proporciones del numero aureo. Los numeros de esta sucesion siguen la siguiente\
   # logica:
   # n = n-2 + n-1
   # Es decir, dada la secuencia de Fibonacci, sabemos que un numero cualquiera dentro de esta sucesion es igual a la suma de los dos numeros anteriores a el (dentro)
   # de la sucesion.
   
   # Basandome en esta logica:
   
   try:
      
      if numero_usuario == 1 or numero_usuario == 2:
         return True
      
      
      # Genero una lista que contenga todos los numeros comprendidos entre 0 y "numero_usuario"
      numeros_comprendidos = list(range(1, numero_usuario))
      
      valorSucesion = 1
      valorActual = 1
      
      print(numeros_comprendidos)
      
      # Recorro la lista de los numeros comprendidos entre ambos valores
      for numero in numeros_comprendidos:
      
         print("numero ==>", numero)
         
         if numero == 1:
            continue
         
         #if valorSucesion == numero_usuario:
         #   valorSucesion = numero_usuario
         #   break
         if numero == (valorSucesion + valorActual):
            
            valorActual = numero
            valorSucesion += valorActual
            
      if (valorSucesion + valorActual) == numero_usuario:
         return True
      else:
         return False
      
   except Exception as e:
      print("Ha ocurrido un error al revisar si el numero proporcionado pertenece a la sucesion de Fibonacci ==> ", e)
 
def es_par(numero_usuario):
   
   """Funcion parametrizada que se encarga de procesar un numero proporcionado por el usuario, y confirmar si se trasta de un numero par o impar.
   
      Args:
        - numero_usuario ==> entero proporcionado por el usuario por teclado.
        
      Returns:
        - boolean ==> booleano que determina si el parametro de la funcion cumple o no la condicion descrita.
   """
   
   # INFO. Un numero "par" es aquel que es divisible entre 2. En caso de que no lo sea, nos referimos a este como "impar".
   try:
      if numero_usuario % 2 == 0:
         return True
      else:
         return False
      
   except Exception as e:
      print("Ha ocurrido un error al revisar si el numero proporcionado por el usuario es un numero par o impar ==> ", e)



if __name__ == "__main__":
   
   while True:
   
      # Se indica al usuario que proporcione un entero por teclado
      numero_usuario = int(input("Por favor, indica un numero cualquiera para obtener un resultado:"))
      print(f"El numero introducido es: {numero_usuario} . Es correcto?")
      
      respuesta_usuario = input("Indica una opcion: SI (1)    NO (2)")
      
      if respuesta_usuario == "SI" or respuesta_usuario == "1":
         
         respuesta_primo = es_primo(numero_usuario)
         
         if respuesta_primo == True:
            respuesta_primo_final = "es primo"
         else:
            respuesta_primo_final = "no es primo"
            
            
         respuesta_fibonacci = pertenece_sucFibonacci(numero_usuario)
         
         if respuesta_fibonacci == True:
            respuesta_fibonacci_final = "fibonacci"
         else:
            respuesta_fibonacci_final = "no es fibonacci"
            
            
         respuesta_paridad = es_par(numero_usuario)
         
         if respuesta_paridad == True:
            respuesta_paridad_final = 'es par'
         else:
            respuesta_paridad_final = "es impar"
            
            
         print(f"{numero_usuario} {respuesta_primo_final}, {respuesta_fibonacci_final} y {respuesta_paridad_final}")
         
         
         print(".")
         print("..")
         print("...")
         
         probar_otra = input("Quieres probar con otro numero? Indica uno de estos valores:  SI (1)      NO (2)")
         
         if probar_otra == "SI" or probar_otra == "1":
            continue
         elif probar_otra == "NO" or probar_otra == "2":
            print("Un placer haber jugado contigo!")
            break
         else:
            print('No se ha reconocido la respuesta indicada.')
            break
      
      else:
         print('Por favor, indica entonces un numero diferente.')
   