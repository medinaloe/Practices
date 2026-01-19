
"""En un restaurante el menú consta de las siguientes opciones:
Ensalada mixta ———————— 12 EU
Sopa de pescado ——————— 10 EU
Dorada al horno ———————— 18 EU
Arroz al curry ————————— 14 EU
Lasaña de carne ——————— 15 EU
Brownie de chocolate ————— 8 EU
Helado ——————————— 6 EU
Refrescos —————————— 5,5 EU
Café ———————————— 3,5 EU
Escribe un script que lea la cantidad de cada alimento consumido y que calcule e imprima el total
de la cuenta."""


Ensalada_mixta, Sopa_de_pescado, Dorada_al_horno, Arroz_al_curry, Lasaña_de_carne, Brownie_de_chocalate, Helado, Resfrescos, Cafe = 12, 10, 18, 14, 15, 8, 6, 5.5, 3.5

Cantidad_Ensalada_mixta = int (input("¿Cuantas Ensaladas mixtas van a tomar?"))
Cantidad_Sopa_de_pescado = int (input("¿Cuantas Sopas de Pescado van a tomar?"))
Cantidad_Dorada_al_horno = int (input("¿Cuantas Doradas al Horno van a tomar?"))
Cantidad_Arroz_al_curry = int (input("¿Cuanto Arroz al Curry van a tomar?"))
Cantidad_Lasaña_de_carne =int (input("¿Cuanta Lasaña de Carne van a tomar?"))
Cantidad_Brownie_de_chocalate =int (input("¿Cuantos Brownis de Chocolate van a tomar?"))
Cantidad_Helado =int (input("¿Cuantos Helados van a tomar?"))
Cantidad_Resfrescos =int (input("¿Cuantos Refrescos van a tomar?"))
Cantidad_Cafe =int (input("¿Cuanto Cafe van a tomar?"))

Precio_total = Cantidad_Ensalada_mixta * Ensalada_mixta + \
Cantidad_Sopa_de_pescado * Sopa_de_pescado + \
Cantidad_Dorada_al_horno * Dorada_al_horno + \
Cantidad_Arroz_al_curry * Arroz_al_curry + \
Lasaña_de_carne * Cantidad_Lasaña_de_carne + \
Cantidad_Brownie_de_chocalate * Brownie_de_chocalate + \
Cantidad_Helado * Helado + Cantidad_Resfrescos * Resfrescos + \
Cantidad_Cafe * Cafe

print ("El precio total seria de ", Precio_total," euros")