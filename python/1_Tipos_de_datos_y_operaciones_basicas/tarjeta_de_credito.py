
"""Crea un script que reciba como input un número de tarjeta de crédito e imprima por pantalla todos
los caracteres en forma de asterisco salvo los últimos cuatro. Si por ejemplo el número de tarjeta
es 1234 2345 3456 5678, el output deberá ser **** **** **** 5678."""

numero_tarjeta = input("Introduzca el número de su tarjeta de crédito, recuerde que esta debe de tener 16 digitos.")


print ( "**** **** **** ", numero_tarjeta [12 : 16])

#OTRA MANERA DE REALIZAR

longitud=(len(numero_tarjeta))
print ("*" * (longitud-4) + numero_tarjeta [longitud-4 : longitud])