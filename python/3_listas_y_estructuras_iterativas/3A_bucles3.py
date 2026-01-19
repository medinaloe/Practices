""" Crea un script que pida al usuario una palabra y luego muestre por pantalla una a una las letras
de la palabra introducida empezando por la última. """

palabra =str (input("Escriba una palabra: "))
long = len(palabra)

for i in range (0, long, 1):
    str (print(palabra[i]))