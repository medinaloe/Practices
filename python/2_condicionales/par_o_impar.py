"""Crea un script que dado un número y una potencia compruebe si ese numero elevado a esa
potencia es par o impar. (Pista: los números pares tiene resto = 0 al dividirlos por 2)"""

numero = float (input("Escribe un numero "))
potencia = float (input("Escribe un numero para realizar una potencia sobre el anterior "))

operacion = numero ** potencia

if operacion % 2 == 0:
    print ("La potencia de ese numero es par")
else:
    print ("La potencia de ese numero es impar")