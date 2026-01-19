""" Escribe un programa que pida al usuario un número entero y muestre por pantalla una
estructura como la de más abajo, donde el valor de entrada es el número de estrellas en el
centro de la estructura.

*
**
***
****
*****
****
***
**
* 

"""


numero = int (input("Escribe un numero entero: "))


for i in range (1, numero +1):
    print("*" * i)
for i in range(numero -1, 0, -1):
    print("*" * i)