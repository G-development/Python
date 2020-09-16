def sommatriceInarrestabile(lista):
    risultato = 0
    for numero in lista:
        risultato += numero
    print ("Il numero della somma è: " + str(risultato))

def moltiplicatriceInarrestabile(lista):
    risultato = 1
    for numero in lista: 
        if numero != 0:
            risultato *= numero
    print ("Il numero della moltiplicazione è: " + str(risultato))

