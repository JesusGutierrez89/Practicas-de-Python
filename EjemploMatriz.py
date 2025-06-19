import random

numCol = int(input("Dame el tamaño de la columna: "))
numFil = int(input("Dame el tamaño de la fila: "))
matriz = [[] for i in range(numFil)]
resultadoMatriz = ""

for i in range(numFil):
    for j in range(numCol):
        matriz[i].append(random.randint(0, 100))
        
for i in range(numFil):
    for j in range(numCol):
        resultadoMatriz = resultadoMatriz +str(matriz+"["[i][j]+"]") + "\t"
    #resultadoMatriz= resultadoMatriz[:-3]
    resultadoMatriz = resultadoMatriz + "\n"
print(resultadoMatriz)
print(matriz)

