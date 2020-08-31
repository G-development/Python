#https://www.programmareinpython.it/esercizi-python/

def max2numeri ():
    print("Inserisci valore uno:")
    x = input()
    print("Inserisci valore due:")
    y = input()
    
    if x == y:
        print("Numeri uguali")
    elif x > y:
        print(x + " è più grande")
    else:
        print(y + " è più grande")

    print("Il più grande è " + max(x,y))

def max3numeri():
    x = input("Uno:")
    y = input("Due:")
    z = input("Tre:")

    print(max(x,y,z))

def seiUnaVocale():
    vocali = "aeiou"
    x = input("Inserisci un carattere:")
    if x in vocali:
        print(x + " è una vocale")
    else:
        print(x + " non lo è")

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

def stringReverser():
    stringa = input("Inserisci una stringa: ")
    index = (len(stringa)-1)
    stringaNuova = ""
    while index >= 0:
        stringaNuova += stringa[index]
        index -= 1

    print(stringaNuova)

def checkPalindromo():
    parola = input("Inserisci parola:")
    index = (len(parola)-1)
    nuovaParola = ""
    while index >= 0:
        nuovaParola += parola[index]
        index -= 1
    if nuovaParola == parola:
        print("Parola palindroma! :)")
    else:
        print("Parola non palindroma! :(")

def creaIstogramma(lista):
    for numero in lista:
        print("*" * numero)

def aCiascunoIlSuo(listaA):
    listaB = []
    for parola in listaA:
        listaB.append(len(parola))
    print(listaB)

def maggioreFraTutti(lista):
    maggiore = 0
    for numero in lista:
        if numero > maggiore: maggiore = numero
    print("Il maggiore è: " + str(maggiore))

    #print("Il maggiore è: " + max(lista))

def linguaggioFurfanti():
    vocali = "aeiou"
    newParola = ""
    parola = input("Inserisci parola:")
    for x in parola:
            if x in vocali:
                newParola += x 
            else:
                newParola = newParola + x + "o" + x
    print (newParola)

def checkValoreInLista(valore, lista):
    print("Ok, in lista!") if valore in lista else print("No, non presente!")

def frequenzimetro():
    stringa = input("Inserisci una stringa!")
    mappa = {}
    for carattere in stringa:
        if carattere in mappa:
            mappa[carattere] += 1
        else:
            mappa[carattere] = 1
    print(f"La mappa è: {mappa}")

def geometra():
    scelta = input('''Scegli quale area calcolare! 
    1- Cerchio
    2- Quadrato
    3- Rettangolo
    4- Triangolo
    5- Esci
    ''')
    if int(scelta) == 1:
        print("Hai scelto calcolo dell'area del cerchio!")
        sceltaCerchio = input("Vuoi calcolarla con: 1- Il raggio, 2- Il diametro, 3- Circonferenza?")
        if int(sceltaCerchio) == 1:
            raggioCerchio = float(input("Inserisci il raggio: "))
            areaCerchioRaggio = 3.14*(raggioCerchio**2)
            print(f"L'area del cerchio, calcolata con il raggio è: {areaCerchioRaggio}" )

        if int(sceltaCerchio) == 2:
            diametroCerchio = float(input("Inserisci il diametro: "))
            areaCerchioDiametro = ((3.14*(diametroCerchio**2))/4)
            print(f"L'area del cerchio, calcolata con il diametro è: {areaCerchioDiametro}")

        if int(sceltaCerchio) == 3:
            circonferenzaCerchio = float(input("Inserisci la circonferenza: "))
            areaCerchioCirconferenza = (circonferenzaCerchio**2)/(4*3.14)
            print(f"L'area del cerchio, calcolata con la circonferenza è: {areaCerchioCirconferenza}")

    if int(scelta) == 2:
        print("Hai scelto calcolo dell'area del quadrato!")
        latoQuadrato = float(input("Inserisci lato del quadrato:"))
        print(f"L'area del quadrato di lato '{latoQuadrato}' è {latoQuadrato**2}")

    if int(scelta) == 3:
        print("Hai scelto calcolo dell'area del rettangolo!")
        baseRettangolo = float(input("Inserisci la base del rettangolo:"))
        altezzaRettangolo = float(input("Inserisci l'altezza del rettangolo:"))
        print(f"L'area del rettangolo è {baseRettangolo*altezzaRettangolo}")

    if int(scelta) == 4:
        print("Hai scelto calcolo dell'area del triangolo!")
        baseTriangolo = float(input("Inserisci la base del triangolo:"))
        altezzaTriangolo = float(input("Inserisci l'altezza del triangolo:"))
        print(f"L'area del triangolo è: {(baseTriangolo*altezzaTriangolo)/2}")

    if int(scelta) == 5:
        exit
    
    else: 
        print("Scelta errata, ritenta")
        geometra()

def passwordGenerator():
    full_char_table = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~"
    alpha_char_table = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

    sceltaPSW = input('''
    Password generator:
    1- Password semplice? (8 caratteri)
    2- Password difficile? (20 caratteri)
    ''')

    if sceltaPSW == 1:


    if sceltaPSW == 2:
        

    else:
        print("Retry.")
        passwordGenerator()


def main():
    #max2numeri()
    #max3numeri()
    #seiUnaVocale()
    
    #lista = [1,2,3,4,5,6,7,8]
    #sommatriceInarrestabile(lista)
    #moltiplicatriceInarrestabile(lista)
    #creaIstogramma(lista)
    #maggioreFraTutti(lista)
    #valore = 4
    #checkValoreInLista(valore, lista)

    #listaParole = ["ciao", "come", "stai"]
    #aCiascunoIlSuo(listaParole)

    #stringReverser()
    #checkPalindromo()
    #linguaggioFurfanti()
    #frequenzimetro()
    geometra()






if __name__ == "__main__":
    main()
    