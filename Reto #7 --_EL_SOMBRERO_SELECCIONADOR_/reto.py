
# Resolucion del reto #60 ==> EL SOMBRERO SELECCIONADOR"

"""
/*
 * Crea un programa que simule el comportamiento del sombrero selccionador del
 * universo mágico de Harry Potter.
 * - De ser posible realizará 5 preguntas (como mínimo) a través de la terminal.
 * - Cada pregunta tendrá 4 respuestas posibles (también a selecciona una a través de terminal).
 * - En función de las respuestas a las 5 preguntas deberás diseñar un algoritmo que
 *   coloque al alumno en una de las 4 casas de Hogwarts:
 *   (Gryffindor, Slytherin , Hufflepuff y Ravenclaw)
 * - Ten en cuenta los rasgos de cada casa para hacer las preguntas
 *   y crear el algoritmo seleccionador:
 *   Por ejemplo, en Slytherin se premia la ambición y la astucia.
 */
"""

# IMPORTS

import time

# Para llevar a cabo el reto, voy a hacer una lista de las cualidades que premia cada una de las casas de magos en la saga de Harry Potter.

"""
Gryffindor. Gryffindor se caracteriza por su valentía, coraje, determinación y caballerosidad.
Los miembros de esta casa son conocidos por su disposición para enfrentar desafíos,
proteger a los más vulnerables y luchar por lo que creen que es justo.


Slytherin. Slytherin valora la astucia, la ambición, el ingenio y el liderazgo.
Los slytherins son conocidos por su determinación para alcanzar el éxito y su habilidad
para sacar provecho de las situaciones a su favor.

Hufflepuff. Hufflepuff valora la lealtad, la amistad, la honestidad y el trabajo duro. 
Los hufflepuffs son conocidos por su generosidad y su disposición a ayudar a los demás sin esperar reconocimiento.

Ravenclaw. Ravenclaw valora la sabiduría, la inteligencia, la creatividad y la curiosidad intelectual.
Los ravenclaws son conocidos por su amor por el conocimiento y su búsqueda constante de respuestas.
"""


# Para el ejemplo, el sombrero seleccionador hara un total de 10 preguntas, para incluir algo mas de seriedad.
# Las preguntas las tomare de https://psycatgames.com/es/quiz/pottermore/ , al igual que las posibles respuestas a las mismas. 

# P1. ¿Cuál de las siguientes opciones odiaría más que la gente lo llamara? Egoista, Ordinario, Ignorante, Cobarde.
# P2. Se colocan cuatro cajas ante ti. ¿Cuál probarías y abrirías?
# P3. El sonido de qué instrumento te gusta más? Piano, trompeta, violin, tambores.
# P4. Blanco o negro? Blanco, negro
# P5. Una vez cada siglo, el arbusto Flutterby produce flores que adaptan su aroma para atraer a los desprevenidos. Si te atrajera, olería a: Una chimenea crepitante, pergamino fresco, hogar, el mar. 
# P6. Después de su muerte, ¿qué le gustaría que hicieran las personas cuando escuchen su nombre?
# P7. ¿Cuál de las siguientes opciones te gustaría estudiar más? Centauros, Vampiros, Trolls, Duendes, Fantasmas, Merpeople, Hombres lobo.
# P8. Si inventaras una poción, ¿qué te daría la poción? Poder, Gloria, Sabiduria, Amor
# P9. Bosque o rio? Bosque, rio.
# P10. ¿Cómo te gustaría ser conocido en la historia? El gran, el sabio, el audaz, el bueno

# Defino una lista con los titulos de cada pregunta

## LISTA PREGUNTAS ##

lista_preguntas = [
    "¿Cuál de las siguientes opciones odiaría más que la gente lo llamara?",
    "Se colocan cuatro cajas ante ti. ¿Cuál probarías y abrirías?",
    "El sonido de qué instrumento te gusta más?",
    "Blanco o negro?",
    "Una vez cada siglo, el arbusto Flutterby produce flores que adaptan su aroma para atraer a los desprevenidos. Si te atrajera, olería a:",
    "Después de su muerte, ¿qué le gustaría que hicieran las personas cuando escuchen su nombre?",
    "¿Cuál de las siguientes opciones te gustaría estudiar más?",
    "Si inventaras una poción, ¿qué te daría la poción?",
    "Bosque o rio?",
    "¿Cómo te gustaría ser conocido en la historia?"
]


# Basandome en los diferentes atributos que tiene cada casa, voy a definir una serie de contadores, los cuales se incrementaran a medida
# que el usuario seleccione una determinada respuesta para cada una de las preguntas que formulara el sombrero.

## CONTADORES ##

determinacion = 0 # Contador para Gryffindor
ingenio = 0 # Contador para Slytherin
amistad = 0 # Contador para Hafflepuff
inteligencia = 0 # Contador para Ravenclaw

## LISTA CONTADORES ##

lista_contadores = [determinacion, ingenio, amistad, inteligencia]


## DICCIONARIO CASAS ##

dict_casas = {
    determinacion: "Gryffindor",
    ingenio: "Slytherin",
    amistad: "Hafflepuff",
    inteligencia: "Ravenclaw"
}

# A continuacion, defino una lista de diccionarios, que representara el conjunto de preguntas, junto con sus posibles respuestas.
# Es este paso, la asignacion de cada uno de los atributos para las respuestas va a ser un poco arbitraria. Hay preguntas que, 
# a menos que se estudien a ciencia cierta, no se sabre de primera instancia que valor representa cada respuesta.
# No obstante, cada una de las respuesta representara a uno de los valores, de modo que, para cada pregunta, no habran respuestas con valores
# repetidos NI faltantes, a excepcion de preguntas con un numero de respuestas diferente de 4.

## LISTA RESPUESTAS ##

dict_respuestas = {
    "respuestas_p1": {
        1: "Egoista.",
        2: "Ordinario.",
        3: "Ignorante.",
        4: "Cobarde."
    },
    "respuestas_p2": {
        1: "El ataúd dorado adornado, de pie sobre patas con garras, cuya inscripción advierte que tanto el conocimiento secreto como la tentación insoportable se encuentran dentro.",
        2: "La reluciente caja de color negro azabache con una cerradura y una llave plateadas, marcada con una runa misteriosa que sabes que es la marca de Merlín.",
        3: "La pequeña caja de carey, adornada con oro, dentro de la cual una pequeña criatura parece estar chillando.",
        4: "La pequeña caja de peltre, sencilla y sencilla, con un mensaje rayado que dice: 'Me abro sólo para los dignos.'."
    },
    "respuestas_p3": {
        1: "Piano.",
        2: "Trompeta.",
        3: "Violin.",
        4: "Tambores."
    },
    "respuestas_p4": {
        1: "Blanco.",
        2: "Negro."
    },
    "respuestas_p5": {
        1: "Una chimenea crepitante.",
        2: "Pergamino fresco.",
        3: "Hogar.",
        4: "El mar."
    },
    "respuestas_p6": {
        1: "Pide mas historias sobre tus aventuras.",
        2: "Te extraña, pero sonríe.",
        3: "No me importa lo que la gente piense de mi después de mi muerte; es lo que piensan de mi mientras estoy vivo lo que cuenta.",
        4: "Piensa con admiración en tus logros."
    },
    "respuestas_p7": {
        1: "Centauros.",
        2: "Vampiros.",
        3: "Trolls.",
        4: "Duendes.",
        5: "Fantasmas.",
        6: "Merpeople.",
        7: "Hombres lobo."
    },
    "respuestas_p8": {
        1: "Poder.",
        2: "Gloria.",
        3: "Sabiduría.",
        4: "Amor."
    },
    "respuestas_p9": {
        1: "Bosque",
        2: "Rio"
    },
    "respuestas_p10": {
        1: "El gran.",
        2: "El sabio.",
        3: "El audaz.",
        4: "El bueno."
    }
}

# Una vez tengo creado el diccionario con las respuestas de cada pregunta, voy a crear un nuevo diccionario con los valores que representan cada pregunta

dict_valores = {      # determinacion, ingenio, amistad, inteligencia
    "respuestas_p1": {
        1: "amistad",
        2: "ingenio",
        3: "inteligencia",
        4: "determinacion"
    },
    "respuestas_p2": {
        1: "ingenio",
        2: "inteligencia",
        3: "amistad",
        4: "determinacion"
    },
    "respuestas_p3": {
        1: "inteligencia",
        2: "amistad",
        3: "ingenio",
        4: "determinacion"
    },
    "respuestas_p4": {          
        1: "amistad, determinacion",
        2: "ingenio, inteligencia"
    },
    "respuestas_p5": {
        1: "determinacion",
        2: "inteligencia",
        3: "ingenio",
        4: "amistad"
    },
    "respuestas_p6": {
        1: "determinacion",
        2: "amistad",
        3: "inteligencia",
        4: "ingenio"
    },
    "respuestas_p7": {
        1: "ingenio",
        2: "inteligencia",
        3: "amistad",
        4: "ingenio",
        5: "determinacion",
        6: "amistad",
        7: "determinacion"
    },
    "respuestas_p8": {
        1: "determinacion",
        2: "ingenio",
        3: "inteligencia",
        4: "amistad"
    },
    "respuestas_p9": {
        1: "ingenio, determinacion",
        2: "amistad, inteligencia"
    },
    "respuestas_p10": {
        1: "determinacion",
        2: "inteligencia",
        3: "ingenio",
        4: "amistad"
    }
}

# Lo que hacermos ahora, sera comenzar el flujo normal del programa, que contendra la logica necesaria para llevar a cabo el proceso completo de muestra, recoleccion
# y representacion de los resultados al usuario.

if __name__ == "__main__":
    
    # Comienzo con un saludo del sombrero seleccionador al usuario.
    print("Muy buenas! Estás a punto de comenzar tu viaje como mago.", end='\n')
    time.sleep(3)
    print("¡Espero que estes listo para el largo camino que te espera!", end='\n')
    time.sleep(3)
    
    print("Antes comenzar tu viaje como mago, deberás acceder a una de las cuatro casas que caracterizan la escuela de Hogwarts.", end='\n')
    time.sleep(3)
    print("¿Estás listo para que, como Sombrero Seleccionador, te haga algunas preguntas?", end='\n')
    time.sleep(2)
    print("Me ayudarán a decidir en que casa deberías de entrar.", end='\n')
    print()
    
    print("*** SELECCIONA UNA OPCIÓN ***", end='\n')
    print()
    print("1. ¡Estoy listo!", end='\n')
    print("2. Creo que me lo voy a pensar mejor.", end='\n')
    print()
    print()
    
    respuesta = input("¿Qué opción escoges?")
    
    if respuesta == "1":
        print("¡Comenzemos, pues! ¡No hay tiempo que perder!", end='\n')
        print()
        print("*"*50)
        print()
        print()
        
        contador_preguntas = 1
        
        for indice_preguntas, pregunta in enumerate(lista_preguntas):
            print(f"Pregunta n{contador_preguntas}:", end="\n")
            print()
            print(pregunta)
            contador_preguntas +=1
            
            for indice_respuestas, grupo_respuestas in enumerate(dict_respuestas):
                
                if indice_preguntas == indice_respuestas:
                    for clave, valor in dict_respuestas[grupo_respuestas]:
                        print(f"{clave}. {valor}")
                    else:
                        # Tras haber mostrado las posibles respuestas...
                        respuesta_usuario = input("¿Cual es tu respuesta?")
                        respuesta_usuario_procesada = int(respuesta_usuario)  # Casteo la respuesta del usuario
                        
                        # Utilizo la respuesta del usuario para aumentar el contador del valor correspondiente
                        for indice_valores, grupo_valores in enumerate(dict_valores):
                            if indice_respuestas == indice_valores:
                                for clave, valor in dict_valores[grupo_valores]:
                                    if clave == respuesta_usuario_procesada:
                                        valores_respuesta_usuario = dict_valores[grupo_valores][clave]  # valor/es de la respuesta del usuario
                                        
                                        # El siguiente proceso solo es util en caso de que la respuesta del usuario contemple dos valores
                                        valores_respuesta_usuario = valores_respuesta_usuario.split(", ")
                                        for valor in valores_respuesta_usuario:
                                            if valor in lista_contadores:
                                                lista_contadores[valor] +=1
                                    
                        
                        
                        
                        time.sleep(1)
                        print(".")
                        time.sleep(1)
                        print("¡Siguiente pregunta!")
                        
        else:
            # Escojo cual es el resultado del sombrero seleccionador
            valor_resultado = max(lista_contadores)
            casa_seleccionada = dict_casas[valor_resultado]
            logitud_casa_seleccionada = len(casa_seleccionada)
            
            print()
            print()
            print("*"*50)
            print()
            print()
            time.sleep(1)
            print("Fiuh! Eso han sido unas cuantas preguntas! Y buenas respuestas, por cierto. No me cabe la menor duda de que te convertiras en un gran mago.", end="\n")
            print()
            time.sleep(1)
            print("Ha llegado el momento que estabas esperando. Ya se cual es la casa en la que creceras!")
            print()
            time.sleep(1)
            print("Has sido seleccionado por...")
            time.sleep(1)
            print(".")
            time.sleep(1)
            print("..")
            time.sleep(1)
            print("...")
            time.sleep(1)           
            
            print()
            print()
            
            # Formateo el mensaje final
            
            TAMANIO_CARTEL = 20
            
            espacio_restante = TAMANIO_CARTEL - logitud_casa_seleccionada
            mitad_espacio_restante = (espacio_restante - 2) // 2
            
            print("#"*TAMANIO_CARTEL)
            print("#" + " "*18+ "#")
            print("#" + " "*mitad_espacio_restante + f"{casa_seleccionada.upper()}" + " "*mitad_espacio_restante + "#")
            print("#" + " "*18+ "#")             
            print("#"*TAMANIO_CARTEL)
        
        
        
        
    elif respuesta == "2":
        print("Vaya, en otro momento sera.", end='\n')
        
    
    