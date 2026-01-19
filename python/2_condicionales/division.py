"""Escribir un programa que pida al usuario dos números y muestre por pantalla su división. Si el
divisor es cero el programa debe mostrar un error."""

numero_1 = float (input("Escribe un numero"))
numero_2 = float (input("Escribe un numero para dividir el anterior"))
total= numero_1 / numero_2


if  numero_1 % numero_2 == 0:
    print ("Error de programa")
else:
    print(numero_1, "/ ", numero_2, "= ", total )
