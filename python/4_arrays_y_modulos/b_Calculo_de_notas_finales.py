""" CALCULO DE NOTAS FINALES
Supongamos que tienes un conjunto de calificaciones de un grupo de estudiantes en un
curso. Cada estudiante tiene cuatro calificaciones: dos exámenes, un trabajo final y una
participación en clase. Quieres calcular la nota final de cada estudiante, donde los
exámenes valen un 30% cada uno, el trabajo final vale un 30% y la participación en clase
vale un 10%. Para ello, puedes usar NumPy para crear un array de 4 columnas y n filas,
donde n es el número de estudiantes. Cada columna representa una de las calificaciones
y cada fila representa un estudiante. Luego, puedes usar operaciones de NumPy para
calcular la nota final de cada estudiante y almacenarla en un nuevo array de una sola
columna. """

import numpy as np

n = int(input("¿Cuántos estudiantes son? "))

calificaciones = []

for i in range(n):
    print("\nEstudiante {i+1}:")
    ex1 = float(input("  Examen 1: "))
    ex2 = float(input("  Examen 2: "))
    trabajo = float(input("  Trabajo final: "))
    participacion = float(input("  Participación: "))
    
    # Guardamos las calificaciones en una lista
    calificaciones.append([ex1, ex2, trabajo, participacion])

# Convertir a array 
calificaciones = np.array(calificaciones)

print("\nNotas finales:")

for i in range(n):
    examen1 = calificaciones[i,0]
    examen2 = calificaciones[i,1]
    trabajo = calificaciones[i,2]
    participacion = calificaciones[i,3]

    # Calcular la nota final manualmente
    nota_final = (examen1 * 0.3) + (examen2 * 0.3) + (trabajo * 0.3) + (participacion * 0.1)

    print(f"Estudiante {i+1}: {nota_final:.2f}")
