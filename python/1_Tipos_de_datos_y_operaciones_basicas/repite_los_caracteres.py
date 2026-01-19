"""Crea un script que acepte un string de 5 caracteres y devuelva otro string con todos los caracteres
duplicados. Si el input es ‘sbc56’, el output deberá ser ‘ssbbcc5566"""

palabra = input ("Ingresa una palabra de 5 caracteres")
print (palabra[0] * 2 + palabra[1] * 2 + palabra[2] * 2 + palabra[3] * 2 + palabra[4] * 2)