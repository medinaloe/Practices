"""Crea un programa en el que se pregunte al usuario por una frase y una letra, y muestre por
pantalla el número de veces que aparece la letra en la frase."""

frase = str (input ("Escribe una frase: "))
letra = str (input ("Escribe la letra que quieres encontrar en la frase escrita:"))
cantidadencontrada = int ()

for caracter in frase:
   if caracter == letra:
    cantidadencontrada = cantidadencontrada + 1 
    
print ("La letra ",letra," aparece ", cantidadencontrada, "veces en la frase.")