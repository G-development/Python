def frequenzimetro():
    stringa = input("Inserisci una stringa!")
    mappa = {}
    for carattere in stringa:
        if carattere in mappa:
            mappa[carattere] += 1
        else:
            mappa[carattere] = 1
    print(f"La mappa è: {mappa}")