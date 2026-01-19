"""
Una compañía de automóviles vende tres tipos de coche: RBM Serie 1, RMB Serie plus, RBM
todoterreno. Cada uno de estos coches tiene un precio de venta y el vendedor recibe una
comisión diferente por cada tipo de coche que ha vendido.
Suponga que los precios y las comisiones son:
RBM Serie 1:
precio: 20.000 EU, comisión: 3%
RMB Serie plus:
precio: 35.000 EU, comisión: 5%
RBM todoterreno:
precio: 60.000 EU, comisión: 7%
Crea un programa donde el usuario introduzca el numero de coches vendidos de cada tipo ese
mes y que le devuelva la cantidad en euros a comisionar ese mes.
"""

print ("Escriba el numero de coches vendidos este mes para ver su comision total.")

ventas_Serie_1 = float ( input ("Serie 1 "))
ventas_Serie_Plus = float (input ("Serie Plus "))
ventas_Todoterreno = float (input ("todoterreno "))

Serie_1 = float (20000)
Serie_Plus = float (35000)
Todoterreno = float (60000)

total_ventas_Serie_1 = Serie_1 * ventas_Serie_1 * 0.03
total_ventas_Serie_Plus = Serie_Plus * ventas_Serie_Plus * 0.03
total_ventas_Todoterreno = Todoterreno * ventas_Todoterreno * 0.03

print ("Este mes has ganado un total de ", total_ventas_Serie_1 + total_ventas_Serie_Plus + total_ventas_Todoterreno , " euros en comisiones")

