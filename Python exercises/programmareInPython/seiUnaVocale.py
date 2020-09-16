def seiUnaVocale():
    vocali = "aeiou"
    x = input("Inserisci un carattere:")
    if x in vocali:
        print(x + " è una vocale")
    else:
        print(x + " non lo è")