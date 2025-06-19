#Diccionario introducir datos por input
calificaciones = {}

n = int(input("¿Cuántos alumnos quieres registrar?: "))

for _ in range(n):
    nombre = input("Nombre del alumno: ")
    nota = float(input(f"Calificación de {nombre}: "))
    calificaciones[nombre] = nota  # Guardar en el diccionario

print("Diccionario de calificaciones:", calificaciones)

###############################################
#Añadir elementos a una lista con input

n = int(input("¿Cuántos datos quieres ingresar? "))
lista = [input(f"Introduce el dato {i+1}: ") for i in range(n)]

print("Lista final:", lista)