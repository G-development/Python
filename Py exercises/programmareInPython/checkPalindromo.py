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