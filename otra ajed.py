def partida_ajedrez(nombre_fichero):

    tablero_inicial = '♜\t♞\t♝\t♛\t♚\t♝\t♞\t♜\n♟\t♟\t♟\t♟\t♟\t♟\t♟\t♟\n\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\n♙\t♙\t♙\t♙\t♙\t♙\t♙\t♙\n♖\t♘\t♗\t♕\t♔\t♗\t♘\t♖'
    tablero =  []
    # Bucle iterativo para recorrer las filas del tablero.partida_ajedrez.
    # i toma como valores los elementos las subcadenas resultantes de partir la cadena del tablero por el caracter de cambio de línea.
    for i in tablero_inicial.split('\n'):
        # Dividimos al tablero la lista que resulta de dividir la subcadena i por el caracter de tabulación.
        tablero.append(i.split('\t'))
    # Abrimos el fichero en modo escritura
    f = open(nombre_fichero, 'w')
    # Bucle iterativo para recorrer las filas del tablero.
    # i toma como valores cada una de las listas (filas) del tablero.
    for i in tablero:
        # Escribirmos cada fila en una línea concatenando los caracteres que contiene.
        f.write('\t'.join(i) + '\n')
    # Cerramos el fichero.
    f.close()
    # Empieza la partida inicializando un contador de movimientos a cero.
    movimiento = 0
    # Bucle condicional para realizar movimientos en la partida hasta que el usario decida terminar.
    while True:
        # Preguntamos al usuario si quiere realizar otro movimiento.
        continuar = input('Deseas hacer otro movimiento (s/n): ')
        # Condicional para ver si el usuario ha respondido si.
        if continuar != 's':
            # Si el usuario no ha contestado que si, salimos del bucle condicional para terminar la partida.
            break
        else:
            # Si el usuario quiere hacer otro movimiento preguntamos por las coordenadas de las casillas de origen y destino.
            fila_origen = int(input('Introduce la fila de la pieza a mover: '))
            columna_origen = int(input('Introduce la columna de la pieza a mover: '))
            fila_destino = int(input('Introduce la fila de destino: '))
            columna_destino = int(input('Introduce la columna de destino: '))
            # Hacemos el movimiento en el tablero
            tablero[fila_destino-1][columna_destino-1] = tablero[fila_origen-1][columna_origen-1]
            tablero[fila_origen-1][columna_origen-1] = ''
            # Incrementamos el contador de movimientos en 1.
            movimiento += 1
            # Abrimos el fichero en modo añadir.
            f = open(nombre_fichero, 'a')
            # Añadimos una cadena con el número de movimiento.
            f.write('Movimiento' + str(movimiento) + '\n')
            # Bucle iterativo para recorrer las filas del tablero.
    # i toma como valores cada una de las listas (filas) del tablero.
            for i in tablero:
                # Escribirmos cada fila en una línea concatenando los caracteres que contiene.
                f.write('\t'.join(i) + '\n')
            # Cerramos el fichero.
            f.close()
    return

partida_ajedrez('partida1.txt')