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