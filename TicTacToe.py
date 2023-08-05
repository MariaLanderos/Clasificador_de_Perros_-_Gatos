from collections import deque


turno = deque(["0", "X"])
tablero =[   #declaramos la variable tablero que es una multilista
    [" ", " ", " "],                #que tendrá cadenas de caracteres
    [" ", " ", " "],
    [" ", " ", " "],
]

def rotar_turno():
    turno.rotate()
    return turno[0]

def mostrar_tablero():
    print("")
    for fila in tablero:    #utilizamos un for que recorra la variable tablero, elemento por elemento 
        print(fila)    #cada elemento es una lista y la imprimirá por completo

def procesar_posicion(posicion):  #va a recibir lo que el usuario haya escrito
    fila, columna = posicion.split(',')
    return[int(fila)-1, int(columna)-1]

#verificamos si cada uno de los rangos están en el rango de 0 a 2
def posicion_correcta(posicion):
    if 0 <= posicion[0] <= 2 and 0 <= posicion[1] <=2:
        if tablero[posicion[0]][posicion[1]] == " ":
            return True
    return False

def actualizar_tablero(posicion, jugador):
    tablero[posicion[0]] [posicion[1]] = jugador


def ganador(j):
    #Se comprueba si alguna de las filas contiene tres símbolos iguales (j) con la condición 
    if tablero[0] == [j,j,j] or tablero[1] == [j,j,j] or tablero[2] == [j,j,j]:
        return True  
    elif tablero[0][0] == j and tablero[1][0] ==j and tablero[2][0] == j:
        return True 
    elif tablero[0][1] == j and tablero[1][1] ==j and tablero[2][1] == j:
        return True 
    elif tablero[0][2] == j and tablero[1][2] ==j and tablero[2][2] == j:
        return True 
    elif tablero[0][0] == j and tablero[1][1] ==j and tablero[2][2] == j:  #revisaremos diagonales
        return True
    elif tablero[0][2] == j and tablero[1][1] ==j and tablero[2][0] == j:  #revisaremos diagonales
        return True
    return False

def juego():
    mostrar_tablero()
    jugador = rotar_turno()
    while True:
        posicion = input("Juega {}. Elige una posición fila, columna de 1 a 3: ".format(jugador))
        if posicion == "salir":
            break
        
        try:
            posicion_l = procesar_posicion(posicion)
        except:
            print("Error, posición {} no es válida".format(posicion))
            continue
        if posicion_correcta(posicion_l):
            print("correcta")
            actualizar_tablero(posicion_l, jugador)  #actualizamos tablero indicando la posicion que se puso y el jugador que lo hizo
            mostrar_tablero()
            
            if ganador(jugador):   #funcion para el ganador
                print("Jugador de {} es el ganador!!".format(jugador))
                break
            
            jugador = rotar_turno()

        else:
            print("Posición {} es incorrecta".format(posicion))



juego()