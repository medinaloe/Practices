
"""El objetivo es crear un programa con el que puedas calcular
tus ahorros anuales. El programa deberá calcular cuánto puede ahorrar una persona dado sus
ingresos por hora, sus horas trabajadas y su gasto de vida semanal."""

"""1. Primero haremos que el programa nos pida nuestro nombre y después imprima un saludo por
pantalla de tipo: ‘Hola <Nombre>’"""

name = input ("Intruduzca su nombre porfavor")
print ("Bienvenido", name)

"""2. Guarda el dinero ganado por hora y las horas trabajadas en la semana en dos variables
diferentes"""

horas_trabajadas_semanales = float (input ("Escriba cuantas horas trabajas a la semana"))
ganado_por_hora = float (input ("Escriba cuanto dinero gana por hora"))

"""3. Multiplica ambas variables para obtener el salario semanal"""

salario_semanal = horas_trabajadas_semanales * ganado_por_hora

"""4. Ahora calcula las ganancias anuales. Guarda el valor en una variable"""

ganancias_anuales = salario_semanal/7 *365

"""5. Ahora imprime por pantalla un mensaje del tipo: ‘<Nombre> tiene unas ganancias anuales de:
<cantidad> euros’"""

print (name, " tiene unas ganancias anuales de", ganancias_anuales, "euros")

"""6. Pide los gastos semanales por pantalla y guárdalos en una variable."""

gastos_semanales = float (input("Escribe los gastos que tienes a la semana"))

"""7. Calcula el gasto anual """

gastos_semanales= gastos_semanales * 3/4

gastos_anuales = gastos_semanales/7 *365



Ahorros_anuales = ganancias_anuales - gastos_anuales

"""Los ahorros anuales serán la resta entre lo ganado durante el año menos los gastos anuales.Imprimir"""

print (name, "obtienes", Ahorros_anuales, "euros de ahorro al año")

