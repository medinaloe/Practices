""" Supongamos que trabajas en una empresa que fabrica dispositivos electrónicos y quieres 
analizar los datos de calidad de los componentes utilizados en la producción de dichos 
dispositivos. Tienes un conjunto de datos que contiene información sobre la fecha de 
producción, el tipo de componente, el lote al que pertenece el componente y la 
puntuación de calidad del componente (un número entre 0 y 100). Quieres analizar estos 
datos para determinar cuál es el tipo de componente con la puntuación de calidad más 
alta, cuántos componentes se produjeron en cada mes y cuál es la puntuación de calidad 
promedio de cada tipo de componente. """
#Identificar el componente con la puntuacion mas alta
import numpy as np
datos = np.array([["2022-01-01","Componente 1","Lote A", 80],
                  ["2022-01-15","Componente 1","Lote B", 90],
                  ["2022-02-01","Componente 2","Lote C", 85],
                  ["2022-02-15","Componente 2","Lote D", 95],
                  ["2022-03-01","Componente 1","Lote E", 75],
                  ["2022-03-15","Componente 2","Lote F", 90],])

tipos_componente = datos[:,1]
tipos_unicos = np.unique(tipos_componente)
calidad = datos[:,3].astype(float)
promedios = np.zeros(len(tipos_unicos))
i = 0
for tipo in tipos_unicos:
    promedios[i] =  np.mean(calidad[tipos_componente == tipo])
    i = i + 1

indice_maximo = np.argmax(promedios)
tipo_mejor_calidad = tipos_unicos[indice_maximo]

print("El tipo de componente con la putuacion de calidad mas alta es:", tipo_mejor_calidad)
#Cuantos componentes se produjeron cada mes

fechas= datos[:,0]
meses, counts = np.unique([fecha[0:7]for fecha in fechas],return_counts = True)
for i in range(len(meses)):
    print("Mes:", meses[i], "Cantidad producida:", counts[i])
    
#Puntuacion de calidad promedio de cada uno de los componentes
promedio_por_tipo = np.zeros(len(tipos_unicos))
for i in range (len(tipos_unicos)):
    promedio_por_tipo[i]= np.mean(calidad[tipos_componente == tipos_unicos[i]])
    print("La puntuacion de calidad promedio para el ", tipos_unicos[i], "es: ", promedio_por_tipo[i])                              