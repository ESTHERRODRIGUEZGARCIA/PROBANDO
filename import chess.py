import chess 
  
board=('♜\t♞\t♝\t♛\t♚\t♝\t♞\t♜\n♟\t♟\t♟\t♟\t♟\t♟\t♟\t♟\n\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\n♙\t♙\t♙\t♙\t♙\t♙\t♙\t♙\n♖\t♘\t♗\t♕\t♔\t♗\t♘\t♖') 
  
print(board)

def partida(tablero):
    board = []

    tablero = board #es una lista puesto que hay que modificarla
    board_list = board.split(" ")
    for i in board_list.split('\n'): #split para separar los elementos del tablero, vertical y horizontalmente
        tablero.append(i.split('\t'))
    print(board_list)
    
    file = open(tablero, "w")

    for i in board:
        file.write('\t'.join(i) + '\n')
        #junto los elementos
    file.close()
    #comienza la partida
    turno = 0 #no se ha jugado todavía
    while True:
        continuar = str(input("¿Quiere seguir jugando? \n Posibles respuestas: Si/No"))
        if continuar == "No":
            break
        elif continuar == "Si": 
            #la pieza está en una posición, el usuario debe moverla
            fila1 = int(input("Introduce la fila en la que está la ficha que quieres mover: "))
            columna1 = int(input("Introduce la columna en la que está la ficha que quieres mover: "))
            fila2 = int(input("Introduce la fila hacia donde quieres mover la ficha: "))
            columna2 = int(input("Introduce la columna donde quieres mover la ficha: "))
            tablero = tablero[fila1 + columna1 + fila2 + columna2]
            turno += 1
            file = open(tablero, "a")
            file.write("Has realizado ", str(turno), "movimientos \n")
            for i in board:
                file.write('\t'.join(i) + '\n')
                #junto los elementos
            file.close()
    return 
partida("1 ")
