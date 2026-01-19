""" Supongamos que tienes un conjunto de datos de clima que contiene información sobre la
temperatura, la humedad y la presión atmosférica en una ciudad durante un año. Quieres
analizar estos datos para determinar cuál fue la temperatura promedio de cada mes, cuál
fue la humedad promedio y la presión atmosférica promedio durante todo el año. Para
ello, puedes usar NumPy para cargar los datos en un array de 3 columnas y n filas, donde
n es el número de mediciones. Luego, puedes usar operaciones de NumPy para filtrar los
datos por mes y calcular las medias de temperatura, humedad y presión atmosférica
correspondientes. """

import numpy as np

datos_climaticos= np.array([
    [20, 70, 1009, 1],
    [18, 75, 1012, 2],
    [16, 72, 1011, 2],
    [19, 73, 1011, 2],
    [22, 65, 1008, 3],
    [25, 60, 1010, 4],
    [22, 60, 1013, 4],
    [24, 59, 1010, 4],
    [25, 61, 1011, 4],
    [28, 50, 1007, 5],
    [30, 45, 1005, 6],
    [10, 45, 1005, 6],
    [32, 40, 1002, 7],
    [30, 35, 1003, 8],
    [33, 35, 1001, 8],
    [32, 35, 1004, 8],
    [31, 45, 1003, 9],
    [28, 50, 1006, 10],
    [27, 48, 1008, 10],
    [25, 60, 1010, 11],
    [22, 70, 1011, 12]
])

temperatura = datos_climaticos[:,0]
humedad = datos_climaticos[:,1]
Presion = datos_climaticos[:,2]
meses = datos_climaticos[:,3]

temperatura_mes = np.zeros(12)
humedad_mes = np.zeros(12)
presion_mes = np.zeros(12)

for i in range (12):
    temperatura_mes[i] = np.mean(temperatura[meses == i+1])
    humedad_mes[i] = np.mean(humedad[meses == i+1])
    presion_mes[i] = np.mean(Presion[meses == i+1])
    print("La temperatura promedia del mes", i+1, "es de:",temperatura_mes[i])
    print("La humedad promedia del mes", i+1, "es de:",humedad_mes[i])
    print("La presion promedio del mes", i+1, "es de:",presion_mes[i])