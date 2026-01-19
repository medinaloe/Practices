"""Crea un script que pida al usuario 3 números diferentes y le indique si alguno de ellos es la suma
de los otros dos. """

numero1 = int ( input ("Escribe un numero: "))
numero2 = int (input ("Escribe un segundo numero: "))
numero3 = int (input ("Escribe un tercer numero: "))

if numero1 + numero2 == (numero3) :
 print ("Sumado el numero 1 y el numero 2 nos da el mismo resultado que el numero 3 que hemos puesto.")
elif numero1 + numero3 == (numero2) :
 print ("Sumado el numero 1 y el numero 3 nos da el mismo resultado que el numero 2 que hemos puesto.")
elif numero2 + numero3 == (numero1):
 print ("Sumado el numero 2 y el numero 3 nos da el mismo resultado que el numero 1 que hemos puesto.")
else :
 print ("Ninguno de los numeros que hemos puesto coincide con la suma de los otros dos.")

