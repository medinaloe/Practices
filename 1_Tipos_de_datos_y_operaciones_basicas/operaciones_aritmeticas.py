#Parte A
"""a. Crea un script que muestre por pantalla el resultado de la siguiente operación aritmética:
((3 + 2) / (2 * 5)) ** 2"""


print (((3+2)/(2*5))**2)

#Parte B
"""b. Escribe un programa que lea un entero positivo, n, introducido por el usuario y después
muestre por pantalla el resultado de la siguiente operación:
n(n + 1)/2"""

print ("Escribe un numero que quieras!!!")
n= float (input (" "))
print ((n*(n + 1))/2)

#Parte C

"""c. Escribe un programa que pida al usuario dos números enteros y muestre por pantalla los
números de entrada, el cociente y el resto. """

numero1 = int (input ("Escribe un numero entero"))
numero2 = int (input ("Escribe otro numero entero"))

Cociente = numero1 // numero2
Resto = numero1 % numero2

print ("El cociente es ", Cociente, " y el resto es ", Resto)