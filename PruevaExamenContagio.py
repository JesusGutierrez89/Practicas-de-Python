import random
fila = int(input("Introduce el tamaño de la fila:"))
columna = int(input("Introduce el tamaño de la columna:"))


def generarCiudad(fila, columna):
    ciudad = []
    for i in range(fila):
        filaCreada = []
        for j in range(columna):
            filaCreada.append("Sano")
        ciudad.append(filaCreada)
    
    f = random.randint(0, fila - 1)
    c = random.randint(0, columna - 1)
    ciudad[f][c] = "I-0"
    
    return ciudad

def mostrarCiudad(ciudad, dia):
    print(f"Día: {dia}")
    for fila in ciudad:
        print(" ".join(fila))
    print("\n")

def contagiar(ciudad):
    dia = 0  
    nuevosContagios = []

    for f in range(len(ciudad)):
        for c in range(len(ciudad[f])):
            if ciudad[f][c] == f"I-{dia}":
                nuevosContagios.append((f, c))
                
    while nuevosContagios:
        mostrarCiudad(ciudad, dia)
        contagiosActuales = nuevosContagios
        nuevosContagios = []
        
        for f, c in contagiosActuales:
            if f > 0 and ciudad[f - 1][c] == "Sano":
                ciudad[f - 1][c] = f"I-{dia + 1}"
                nuevosContagios.append((f - 1, c))
            if f < len(ciudad) - 1 and ciudad[f + 1][c] == "Sano":
                ciudad[f + 1][c] = f"I-{dia + 1}"
                nuevosContagios.append((f + 1, c))
            if c > 0 and ciudad[f][c - 1] == "Sano":
                ciudad[f][c - 1] = f"I-{dia + 1}"
                nuevosContagios.append((f, c - 1))
            if c < len(ciudad[0]) - 1 and ciudad[f][c + 1] == "Sano":
                ciudad[f][c + 1] = f"I-{dia + 1}"
                nuevosContagios.append((f, c + 1))
        
        dia += 1
    mostrarCiudad(ciudad, dia)
        
ciudad = generarCiudad(fila, columna)
mostrarCiudad(ciudad, 0)
contagiar(ciudad)
