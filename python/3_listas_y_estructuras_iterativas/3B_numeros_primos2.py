""" Dado una lista de números enteros, escribe un script en Python que devuelva una nueva lista con
los números primos de la lista original. Además, el script debe devolver el número total de
números primos encontrados y la suma de los números primos encontrados."""

numeros = [2,3,4,5,6,7,8,9]
primos = []
total_primos= 0
suma_primos = 0

for numero in numeros:
    primo = True
    for i in range(2,numero):
        if numero % i == 0 :
            primo = False
    if primo == True:
        primos.append(numero)
        total_primos = total_primos + 1
        suma_primos= suma_primos + numero

print(primos)
print(total_primos)
print(suma_primos)

