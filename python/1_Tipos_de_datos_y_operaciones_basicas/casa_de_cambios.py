"""Crea un script que reciba una cantidad de euros del usuario e imprima 
por pantalla el correspondiente en dólares (considera una tasa de cambio donde 1 EU = 1.2 $) 
"""

print ("¿Cuanta cantidad desea cambiar?")
euros = float (input())
print ("Has introducido " , euros , " euros")

dolar = euros * 1.2
print ("El cambio a dolares es de " , dolar , "$")

"""La casa de cambios se queda un 10% en concepto de ‘tasas de gestión’. Calcula el monto
recibido, el cambio en dólares, la cantidad que se queda la casa de cambios y la cantidad de
dólares restante que recibirá el usuario. Imprime el desglose por pantalla formateado de tal
forma que quede claro para el usuario.
"""

interes = dolar * 0.1
print ("La casa de cambios se queda con un 10%, que es " , interes , "$")
cambiofinal = dolar - interes
print ("El importe final que recibe el cliente es de " , cambiofinal , "$")