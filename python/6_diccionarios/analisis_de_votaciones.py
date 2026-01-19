""" Supongamos que tienes los resultados de una elección con los nombres
de los candidatos y la cantidad de votos obtenidos por cada uno.
Implementa un programa en Python que permita registrar los votos,
mostrar la lista completa de candidatos y sus votos, encontrar al
candidato ganador (con más votos) y calcular el porcentaje de votos que
obtuvo cada candidato """

dict_candidatos={}
continuar = True
#elijo lo que quiero modificar o acceder en el programa
while continuar:
    print("1 -Añade un candidato.")
    print("2 -Registra los votos por candidato.")
    print("3 -Mostrar lista de los candidatos y sus votos.")
    print("4 -Mostrar candidato ganador.")
    print("5 -Mostrar porcentaje de votos de cada candidato.")
    print("6 -Salir o terminar")
    opcion= input("Elije el numero de la opcion que deseas realizar.")
    #Añadir candidatos
    if opcion =="1":
        candidato= input("Escribe el nombre del candidato que quieres añadir:")
        dict_candidatos[candidato]=0
        print(dict_candidatos)
        #Damos nuestras votaciones a los candidatos
    elif opcion=="2":
        voto=input("Ingrese el nombre del candidato al que quiere dar su voto:")
        if voto in dict_candidatos:
            dict_candidatos[voto] =dict_candidatos[voto]+ 1
        else:
            print("El candidato no existe, pruebe de nuevo")
        #Mostramos lista de de votos de cada participante
    elif opcion == "3":
        for candidato,voto in dict_candidatos.items():
            print(f"El candidato: {candidato} tiene un total de: {voto}" "votos.")
        #mostramos el candidato ganador
    elif opcion == "4":
        ganador =max(dict_candidatos.values())
        nombre = max(dict_candidatos, key=dict_candidatos.get)
        print("El ganador a sido", nombre ,"con un total de", ganador ,"votos")
        #mostramos porcentaje de votos
    elif opcion == "5":
        total_votos =sum(dict_candidatos.values())
        for candidato, votos in dict_candidatos.items():
            porcentaje = (votos/total_votos)*100
            print(f"El candidato {candidato} a tenido un porcentaje total de un {porcentaje:.2f} %")     
    elif opcion == "6":
        continuar=False
        
        
        
            
        
        
        
        

    