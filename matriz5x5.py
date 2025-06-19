def crearMatriz():
    matriz = []
    for i in range(5):
        fila = []
        for j in range(5):
            numero = int(input("Ingrese numeros: "))
            fila.append(numero)
        matriz.append(fila)
    return matriz

def mostrarTabla(matriz):
    print("Matriz:")
    for fila in matriz:
        print(fila)

def sumafila(matriz):
    suma_filas = []
    for fila in matriz:
        suma_fila = sum(fila)
        suma_filas.append(suma_fila)  
    return suma_filas


def sumaColumna(matriz):
    suma_columnas = []
    for i in range(5):
        suma_columna = 0
        for j in range(5):
            suma_columna += matriz[j][i]
        suma_columnas.append(suma_columna)
    return suma_columnas

tabla = crearMatriz()
mostrarTabla(tabla)

suma_filas = sumafila(tabla)
suma_columnas = sumaColumna(tabla)

print("Suma de las filas")
for suma in (suma_filas):
    print(f"total filas : {suma}")

print("Suma de las columnas")
for suma in (suma_columnas):
    print(f"total columnas : {suma}")