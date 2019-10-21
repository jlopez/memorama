def juego():
    # Preparacion inicial
    desplegar_bienvenida()
    tablero = generar_tablero()
    jugador_previo = None
    jugador = 1

    # Ciclo principal
    while not tablero_completado():
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