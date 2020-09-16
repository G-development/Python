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