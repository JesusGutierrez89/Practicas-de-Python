#hacer una funcion que pida filas, columnas y bombas
#Pide el tamaño de filas y columnas
#Mete un numero de bombas aleatorio
#Muestra el tablero

import random

def crearTablero(filas, columnas, bombas):
    tablero = []
    for i in range(filas):
        filasCreadas =["-"]*columnas
        tablero.append(filasCreadas)
    cont=0
    while cont < bombas:
        filaBomba = random.randint(0, filas-1)
        columnaBomba = random.randint(0, columnas-1)
        if tablero[filaBomba][columnaBomba] != "*":
            tablero[filaBomba][columnaBomba] = "*"
            cont+=1
    return tablero

filas = int(input("Introduce el numero de filas: "))
columnas = int(input("Introduce el numero de columnas: "))
bombas = int(input("Introduce el numero de bombas: "))

def mostrarTablero(tablero):
    for i in tablero:
        print("", end="\t")
        for e in i:
            print(e, end="\t")
        print("\n")
   
    
mostrarTablero(crearTablero(filas, columnas, bombas))


def jugar(tablero):
    terminar = False
    fila = int(input("Introduce la fila para iniciar el juego: "))
    columna = int(input("Introduce la columna para iniciar el: "))
    puntuacion = 0
    while not terminar:
        if tablero[fila][columna]  == "*":
            print("Has perdido")
            mostrarTablero(tablero)
            terminar = True
            print("Te ha explotado la bomba")
        else:
            print("Sigue jugando")
            puntuacion+=1
            tablero[fila][columna] = "J"
            mostrarTablero(tablero)
            if(tablero[fila][columna] == "-" and tablero[fila][columna] != "*"):
                movimiento()
                mostrarTablero(tablero)
                print("puntuacion:", puntuacion)
            continuar = input("¿Quieres seguir jugando? (s/n): ")
            if continuar.lower() != 's':
                terminar = True

jugar(crearTablero(filas, columnas, bombas))

def movimiento():
    Movimiento= input("Introduce el movimiento: Arriba(1), Abajo(2), Izquierda(3), Derecha(4): ")
    if Movimiento == "1":
        fila -= 1
    elif Movimiento == "2":
        fila += 1
    elif Movimiento == "3":
        columna -= 1
    elif Movimiento == "4":
        columna += 1
    return fila, columna