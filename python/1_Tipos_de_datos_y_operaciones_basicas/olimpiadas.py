"""En la competición de skeleton de las olimpiadas de invierno hay tres finalistas. El cronómetro mide
los siguientes tiempos:
-Hannah Neise: 8 minutos 3 segundos y 10 centésimas
-Jackie Narracott: 12 minutos 7 segundos y 8 centésimas
-Kimberley Bos: 9 minutos 14 segundos y 3 centésimas
"""
"""1. Crea un script que pida los tiempos por pantalla para cada uno de los finalistas """

tiempo_Hannah = input ("Ingresa el tiempo de Hannah Neise: minutos segundos centésimas ")
tiempo_Jackie = input ("Ingresa el tiempo de Jackie Narracott: minutos segundos centésimas ")
tiempo_Kimberly = input ("Ingresa el tiempo de Kimberley Bos: minutos segundos centésimas ")

minutos_Hannah, segundos_Hannah, centesimas_Hannah = tiempo_Hannah.split(" ")
minutos_Jackie, segundos_Jackie, centesimas_Jackie = tiempo_Jackie.split(" ")
minutos_Kimberly, segundos_Kimberly, centesimas_Kimberly = tiempo_Kimberly.split(" ")

"""2. Convierte los tiempos de minutos-segundos-centésimas a segundos"""

tiempo_Hannah = float(minutos_Hannah) * 60 + float(segundos_Hannah) + float(centesimas_Hannah) * 0.01
tiempo_Jackie = float(minutos_Jackie) * 60 + float(segundos_Jackie) + float(centesimas_Jackie) * 0.01
tiempo_Kimberly = float(minutos_Kimberly) * 60 + float(segundos_Kimberly) + float(centesimas_Kimberly) * 0.01

"""3. Sabiendo que la pista es de 100 metros calcula la velocidad media de cada uno de ellos en
metros por segundo. """

velocidad_Hannah = 100/ tiempo_Hannah
velocidad_Jackie = 100/ tiempo_Jackie
velocidad_Kimberly = 100/ tiempo_Kimberly

"""4. Imprime los resultados por pantalla"""

print ("Velocidad media de Hannah", velocidad_Hannah)
print ("Velocidad media de Jackie", velocidad_Jackie)
print ("Velocidad media de Kimberly", velocidad_Kimberly)