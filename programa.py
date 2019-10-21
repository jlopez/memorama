#!/usr/bin/env python3
import random

ANCHO = 6
ALTO = 6


def desplegar_bienvenida(tablero):
    print("Bienvenido al juego memorama")
    print("Aqui esta el tablero")
    mostrar_tablero(tablero)

def generar_tablero():
    numero_celdas = ANCHO * ALTO
    maximo_numero = numero_celdas // 2

    # Genera los numeros que se usaran
    # p. ej. Si el tablero es de 2 * 2,
    # hay 4 celdas, y solo se usa hasta el numero 4/2 = 2
    # Generamos una lista con [1, 2]
    numeros = list(range(1, maximo_numero + 1))

    # Duplicamos esta lista para generar el tablero
    # que sera una lista con los numeros del tablero:
    # p. ej. [1, 2] * 2 = [1, 2, 1, 2]
    # Esto es equivalente a un tablero que tenga estos numeros:
    #
    #      1  2
    #      1  2
    #
    tablero = numeros * 2

    # Ahora revolvemos los numeros usando randomshuffle
    random.shuffle(tablero)

    # El tablero esta listo, lo regresamos
    return tablero

def mostrar_tablero(tablero):
    # Imprimir encabezado de columnas
    print('  ', end=' ')
    for c in range(1, ANCHO + 1):
        print('%2d' % c, end = ' ')
    print()

    # Imprimir celdas
    i = 0
    for r in range(1, ALTO + 1):
        print('%2d' % r, end=' ')
        for c in range(1, ANCHO + 1):
            valor = tablero[i]
            i = i + 1

            # Si la celda tiene un numero positivo quiere decir
            # que aun no ha sido revelado. Si es negativo quiere
            # decir que ya lo fue
            if valor > 0:
                print(' -', end=' ')
            else:
                print('%2s' % -valor, end=' ')
        print()


def tablero_completado(tablero):
    # El tablero esta completado si TODAS las celdas
    # son negativas - quiere decir que todas las celdas
    # han sido reveladas.
    # La funcion all() toma una lista, la cual la creamos
    # aqui, en el momento, usando un codigo llamado
    # "list comprehension". La parte:
    #
    #    celda < 0 for celda in tablero
    #
    # define una lista creada con valores True/False, un valor
    # por cada celda en el tablero. True si la celda es negativa,
    # False si es positiva.
    return all(celda < 0 for celda in tablero)


def anuncia_jugador(jugador):
    print()
    print()
    print("------------------------------------")
    print("Es el turno del jugador %s" % jugador)
    print("------------------------------------")


def obten_jugada_valida(tablero):
    coordenada1 = obten_coordenada_valida(1, tablero)
    # Pedimos la coordenada 2 hasta que nos den una diferente
    while True:
        coordenada2 = obten_coordenada_valida(2, tablero)
        if coordenada1 == coordenada2:
            print("La segunda coordenada no puede ser igual a la primera")
            print("Intente de nuevo...")
        else:
            break
    return [coordenada1, coordenada2]


def obten_coordenada_valida(numero, tablero):
    # Repite el codigo hasta que lo logremos
    while True:
        # Obtenemos el renglon y la columna
        renglon = obten_numero_valido('el renglon', numero, ALTO)
        columna = obten_numero_valido('la columna', numero, ANCHO)

        # Vemos si el valor en esa celda es positivo.
        # Si lo es, lo logramos (break), de lo contrario
        # seguimos preguntando
        i = renglon * ANCHO + renglon
        valor = tablero[i]
        if valor > 0:
            # Exito, el valor es positivo, podemos salir del while
            break
        else:
            # El valor es negativo, pedimos de nuevo
            print("La coordenada (%s, %s) es invalida. Intenta de nuevo..." %
                  (renglon, columna))

    # Regresa la coordenada usando una lista de dos valores
    return [renglon, columna]


def obten_numero_valido(tipo, numero, maximo):
    # Repite el codigo hasta que lo logremos
    while True:
        # Pedimos un valor
        mensaje = 'Dame %s de tu jugada #%d (1-%d): ' % (tipo, numero, maximo)
        valor = int(input(mensaje))

        # Si el valor no esta entre 1 y maximo, pedimos de nuevo
        if valor <= 0 or valor > maximo:
            print("Desafortunadamente %s es invalido. Intenta de nuevo..." % tipo)
        else:
            # El valor fue correcto, salimos del while
            break

    # Regresamos el valor que dio el usuario
    return valor

def aplica_jugada(tablero, jugada):
    # Obtenemos la coordenada 1 y 2 de la jugada
    coordenada1, coordenada2 = jugada

    # Convertimos las coordenadas a indices y obtenemos
    # los valores de ambas celdas
    indice1 = indice_para_coordenada(coordenada1)
    indice2 = indice_para_coordenada(coordenada2)
    valor1 = tablero[indice1]
    valor2 = tablero[indice2]

    # Cambiamos los signos para mostrar los valores
    tablero[indice1] = -valor1
    tablero[indice2] = -valor2

    # Desplegamos el tablero modificado
    print()
    print("Este es el tablero despues de aplicar la jugada")
    mostrar_tablero(tablero)

    # La jugada fue exitosa si los dos valores eran iguales
    # Aqui dice: crea una variable llamada exito, y dale el
    # valor de la comparacion entre valor1 y valor2.
    # Si son iguales, sera True, pero si son diferentes,
    # sera False
    exito = valor1 == valor2

    # Si la jugada no fue exitosa, volvemos a reestablecer
    # los valores (positivos) para "ocultarlos" de nuevo
    if not exito:
        tablero[indice1] = valor1
        tablero[indice2] = valor2

    # Finalmente regresamos el valor de la variable exito
    # para que la funcion principal decida si cambiar de
    # turno
    return exito


def indice_para_coordenada(coordenada):
    # Obten el valor del renglon y la columna de la coordenada
    renglon, columna = coordenada
    # Convierte las coordenadas a un indice dentro del tablero
    # Tenemos que restar uno a las variables porque usamos como
    # origen la posicion 1, 1
    return (renglon - 1) * ANCHO + (columna - 1)


def juego():
    # Preparacion inicial
    tablero = generar_tablero()
    desplegar_bienvenida(tablero)
    jugador_previo = None
    jugador = 1

    # Ciclo principal
    while not tablero_completado(tablero):
        # Anuncia jugador si cambio
        if jugador_previo != jugador:
            anuncia_jugador(jugador)
        jugador_previo = jugador

        # Consigue jugada y aplicala
        jugada = obten_jugada_valida(tablero)
        exito = aplica_jugada(tablero, jugada)

        # Si el jugador no tuvo exito en encontrar cartas,
        # cambia al otro jugador
        if not exito:
            jugador = 2 if jugador == 1 else 1
        else:
            print("Correcto! El jugador %s puede continuar jugando" % jugador)
            print()

juego()
