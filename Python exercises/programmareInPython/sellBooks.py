def sellBooks(libreria, libro):
    #vendi libri
    vendita = False

    if libro in libreria:
        vendita = True
        libreria[libro] -= 1
        print(f"Il libro {libro} è stato venduto!")

        if libreria[libro] == 0:
            del libreria[libro]
    else:
        print(f"Il libro {libro} non è presente nella nostra libreria, lo ordino")
        ordini.append(libro)
        print(f"Da ordinare: {ordini}")
    print(f"La libreria adesso è così composta: {libreria}")
    return vendita