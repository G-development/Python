def maggioreFraTutti(lista):
    maggiore = 0
    for numero in lista:
        if numero > maggiore: maggiore = numero
    print("Il maggiore è: " + str(maggiore))

    #print("Il maggiore è: " + max(lista))