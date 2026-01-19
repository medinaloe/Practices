
""" Una red social tiene una base de datos de usuarios y sus correspondientes amistades. 
Crea un programa que tome una base de datos de una red social como una lista de 
tuplas, donde cada tupla contiene el nombre del usuario y una lista de sus amigos. Los 
nombres repetidos en la lista de amigos corresponden a usuarios con varias cuentas 
diferentes. Deberas eliminar las cuentas duplicadas y después  devolver una tupla de 
tuplas que contiene el número real de amigos por usuario y el usuario con más amigos """

 #Pista 1: Tus datos de entrada podrían ser así  —>  red_social = [("Juan", ["Maria", "Pedro", 
#"Luis"]), ("Maria", ["Juan", “Pedro”,”Juan”]), ("Pedro", ["Juan", "Maria"]), ("Luis", [“Juan”])] 
#Pista 2: Para eliminar duplicidades puedes usar sets 


red_social = [("Juan", ["Maria", "Pedro", "Luis"]), ("Maria", ["Juan", "Pedro","Juan"]), ("Pedro", ["Juan", "Maria"]), ("Luis", ["Juan"])]
red_sin_duplicados=[]
#Quitamos los duplicados de las tuplas
for usuarios, amigos in red_social:
    amigos_sin_duplicados= list(set(amigos))
    red_sin_duplicados.append((usuarios,amigos_sin_duplicados))
print(red_sin_duplicados)
#Contamos cuantos amigos tiene cada usuario
amigo_cada_usuario= []
for usuarios, amigos in red_sin_duplicados:
    amigo_cada_usuario.append((usuarios,len(amigos)))
amigo_cada_usuario=tuple(amigo_cada_usuario)
print(amigo_cada_usuario)
#Obtener el usuario con mas amigos
lista_usuarios = [tupla[0] for tupla in amigo_cada_usuario]
numeros_amigos = [tupla[1] for tupla in amigo_cada_usuario]
indice_con_mas_amigos= numeros_amigos.index(max(numeros_amigos))
usuario_con_mas_amigos= lista_usuarios[indice_con_mas_amigos]
print("El usuario con mas amigos es", usuario_con_mas_amigos)