import random
filas=5
columnas=5

#Crear matriz 5x5
def crear_matriz(filas, columnas):
    matriz = [[random.randint(1,50) for _ in range(columnas)] for _ in range(filas)]
    return matriz

#mostrar matriz bien
def mostrarMatriz(matriz):
    for f in matriz:
        print("", end="\t")
        for e in f:
            print(e, end="\t")
        print("\n")
        
#matriz transpuesta
def matrizTrasnpuesta(matriz):
    matriz_transpuesta = [[matriz[j][i] for j in range(len(matriz))] for i in range(len(matriz[0]))]
    return matriz_transpuesta

#devolver diagonal
def devolDiagonal(matriz):
    diagonal = []
    for f in range(len(matriz)):
        diagonal.append(matriz[f][f])
    return diagonal

def multiplicarElemento(matriz):
    numero=int(input("Dime el numero que deseas multiplicar los elementos: "))
    multiplicacion =[]
    for fila in matriz:
        nuevaFila = [elemento * numero for elemento in fila]
        multiplicacion.append(nuevaFila)
    return multiplicacion
            
        

matriz = crear_matriz(filas, columnas)
mostrarMatriz(matriz)
print("----------------------------------------------")
mostrarMatriz(matrizTrasnpuesta(matriz))
print("----------------------------------------------")
diagonal = devolDiagonal(matriz)
print("Diagonal de la matriz:")
print(diagonal)
print("----------------------------------------------")
mostrarMatriz(multiplicarElemento(matriz))

