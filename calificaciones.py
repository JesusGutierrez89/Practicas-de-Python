# Genera una lista con las calificaciones de 20 estudiantes (puedes usar números aleatorios entre 0 y 100).
# Implementa las siguientes funciones:
# promedio_calificaciones: Calcula y devuelve el promedio de las calificaciones.
# calificacion_mas_alta: Encuentra y devuelve la calificación más alta.
# calificaciones_aprobadas: Devuelve una lista con todas las calificaciones mayores o iguales a 60.
# cantidad_reprobados: Calcula cuántos estudiantes reprobaron.
# Muestra los resultados al usuario.
import random
#crear lista de calificaciones de 20 estudiantes
calificaciones = [random.randint(0, 100) for i in range(20)]

#promedio de las calificaciones
def promedioCalificaniones(lista):
   suma = sum(lista)
   media = suma / len(lista)
   return media

#calificacion mas alta
def calificacionMasAlta(lista):
    max = 0
    for calificacion in lista:
        if calificacion > max:
            max = calificacion
    return max

#calificaciones aprobadas
def calificacionAprobados(lista):
    aprobados =[]
    suspensos = []
    for calificacion in lista:
        if calificacion >= 60 and calificacion <= 100:
            aprobados.append(calificacion)
        else:
            suspensos.append(calificacion)
    return aprobados

#cantidad de aprobados
def cantidadAprobados(lista):
    cantApro = 0
    for calificacion in lista:
        if calificacion >= 60 and calificacion <= 100:
            cantApro +=1
    return cantApro
    
        
print(f"las calificaciones son: {calificaciones}")
print(f"El promedio de las calificaciones es: {promedioCalificaniones(calificaciones)}")
print(f"La calificacion mas alta es: {calificacionMasAlta(calificaciones)}")
print(f"Las calificaciones aprobadas son: {calificacionAprobados(calificaciones)}")
print(f"La cantidad de aprobados es: {cantidadAprobados(calificaciones)}")
