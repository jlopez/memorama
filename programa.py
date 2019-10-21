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
    for c in range(ANCHO):
        print('%2d' % c, end = ' ')
    print()

    # Imprimir celdas
    i = 0
    for c in range(ANCHO):
        print('%2d' % c, end=' ')
        for r in range(ALTO):
            valor = tablero[i]
            i = i + 1

            # Si la celda tiene un numero positivo quiere decir
            # que aun no ha sido revelado. Si es negativo quiere
            # decir que ya lo fue
            if valor > 0:
                print(' -', end=' ')
            else:
                print('%2s' % -tablero[i], end=' ')
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
    pass

def obten_jugada_valida(tablero):
    pass

def aplica_jugada(tablero, jugada):
    pass


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

juego()
