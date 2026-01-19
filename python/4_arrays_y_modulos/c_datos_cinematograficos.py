""" Supongamos que tienes un conjunto de datos de películas que contiene información 
sobre su título, género, duración, año de lanzamiento y calificación. Quieres analizar 
estos datos para determinar cuál es el género de película más popular, cuántas películas 
se lanzaron en cada década y cuál es la duración promedio de cada género de película. """

import numpy as np
peliculas = np.array ([
    ["Peli 1", "Comedia", 120, 1990,8.5],
    ["Peli 2", "Accion", 110, 2005,7.8],
    ["Peli 3", "Drama", 95, 2010,6.9],
    ["Peli 4", "Comedia", 100, 1985,7.5],
    ["Peli 5", "Accion", 130, 2015,8.1],
    ["Peli 6", "Drama", 110, 2000,6.7],
    ["Peli 7", "Comedia", 90, 1995,8.2],
    ["Peli 8", "Accion", 105, 2010,7.4],
    ["Peli 9", "Drama", 125, 1980,6.8],
    ["Peli 10", "Comedia", 95, 2000,8.0],])
#obtenemos los generos y la cantidad de ellos
generos, conteos = np.unique(peliculas[:,1], return_counts=True)
#Ordenamos los conteos de mayor a menor
conteo_descendente= np.argsort(conteos)[::-1]
#cogemos el conteo mayor que nos a salido ordenado 
genero_mas_popular = generos[conteo_descendente[0]]
print("El genero mas popular es_ ",genero_mas_popular)


#Creamos un array con las decadas que vamos a tratar
decadas = np.unique(peliculas[:,3].astype(int)//10*10)

#Contamos las peliculas por cada decada
conteos_decada = []
for decada in decadas:
    conteo = np.count_nonzero((peliculas[:,3].astype(int)>= decada)&(peliculas[:,3].astype(int)< decada +10))
    conteos_decada.append(conteo)
    print("Se crearon ", conteo, "peliculas en las de cada de ", decada)
    
#duracion media de las peliculas por genero
todos_generos= peliculas[:,1]
duracion_peliculas = peliculas[:,2]
duracion_media = np.zeros(len(generos))

for i in range(len(generos)):
    duracion_media[i]= np.mean(duracion_peliculas[todos_generos == generos[i]].astype(float))
    print("La media de duracion de las peliculas de ", generos[i]," es de ", duracion_media[i])