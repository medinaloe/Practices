"""Crea un script que pida al usuario 4 números diferentes y imprima el mayor de los cuatro por
pantalla"""

numero = input ("Escribe 4 numeros distintos: ")
numero1, numero2, numero3, numero4 = numero.split (" ")

if (numero1 > numero2) :
 numero2, numero1= numero1, numero2
if (numero2 > numero3) :
   numero3, numero2 = numero2, numero3
if (numero3 > numero4) :
  numero4, numero3 = numero3 , numero4
  
  print ("El ", numero4, " es el numero mayor.")
  print (numero1, numero2,numero3, numero4)