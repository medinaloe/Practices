"""Define una lista de 5 palabras aleatorias y una lista de letras prohibidas que contenga tres letras.
Filtra las palabras en tu lista original crea una nueva lista de palabras filtradas que solo contenga
aquellas palabras que no tienen ninguna letra prohibida. """


lista = ["hola", "adios", "mañana", "codo", "termita"]
letras_prohibidas = ["e", "s", "h"]
palabras_filtrasdas = []

for i in lista:
    incluir = True
    for letras_prohibidas in letras_prohibidas:
        if letras_prohibidas in i:
          incluir = False
    if incluir == True:
       palabras_filtrasdas.append(i)

print (palabras_filtrasdas)      
         
     