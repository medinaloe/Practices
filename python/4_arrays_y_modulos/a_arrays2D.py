"""Crea un arrays lleno de 1s con una longitud dada por el usuario """

longitud = int(input("Introduzca la longitud que quieres que sea el array que estas creando:"))
import numpy as np
array = np.ones(longitud)
print(array)

"""Cambia la forma del array para que tenga una estructura de tipo (filas, columnas) """

filas = int(input("Escribe la cantidad de filas que deseas:"))
columnas = int(input("Escribe la cantidad de columnas que deseas:"))

if filas* columnas == longitud:
 array_fc = np.reshape(array, (filas,columnas))
 print("El array con filas y columnas es: \n", array_fc)
else:
    print("La cantidad de filas y columnas no es compatible con la longitud del array.")

"""Crea una “matriz identidad” con la misma forma que el array anterior (filas, columnas) """

matriz_identidad= np.eye(filas,columnas)
print(matriz_identidad)

"""Concatena ambas estructuras horizontalmente y verticalmente
 (Pista: Investiga el funcionamiento de concatenate() y de vstack() y hstack() de numpy) """
 
horizontal=np.concatenate((array_fc,matriz_identidad),axis=1)
print ("La concatenacion horizontal es : \n", horizontal)

vertical= np.concatenate((array_fc,matriz_identidad),axis=0)
print ("La concatenacion vertical es : \n", vertical)

#Otra manera de hacerlo:

horizontal = np.hstack((array_fc,matriz_identidad))
print ("La concatenacion horizontal es : \n", horizontal)

vertical = np.vstack((array_fc,matriz_identidad))
print ("La concatenacion vertical es : \n", vertical)