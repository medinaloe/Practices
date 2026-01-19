
"""Para tributar en un determinado país es necesario ser mayor de edad y cobrar más de 1000 euros
al mes. Además los tramos impositivos de la renta anual son los siguientes:
RENTA TIPO IMPOSITIVO
-Menos de 15.000 eu 5%
-Entre 15.000 y 25.000 eu 15%
-Entre 25.000 y 35.000 eu 20%
-Entre 35.000 y 60.000 eu 30%
-Más de 60.000 eu 45%
Escribe un script que primero compruebe si eres susceptible de que se te aplique algún tipo
impositivo y en caso afirmativo imprima por pantalla cuál te tocaría.  """ 

edad = str (input("Hola buenas, ¿eres mayor de 18 años?(si/no): "))


if edad.lower() == "si":
  sueldo = int (input ("¿Cuanto dinero cobra al mes? "))
  sueldo_total = sueldo * 12
  if sueldo_total< 15000:
   print ("Se te aplicara un impositivo del 5%.")
  elif sueldo_total >= 15000 and sueldo_total < 25000:
   print ("Se te aplicara un impositivo del 15%.")
  elif sueldo_total >= 25000 and sueldo_total < 35000:
   print ("Se te aplicara un impositivo del 20%.")
  elif sueldo_total >= 35000 and sueldo_total < 60000:
   print ("Se te aplicara un impositivo del 30%.")
  elif sueldo_total > 60000:
   print ("Se te aplicara un impositivo del 45%.")
else:
 print ("No es necesario que relice la declarion de la renta.")
