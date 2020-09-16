def timeMaster():
    print("Time Master \nTutto in secondi.")
    giorni = int(input("Inserisci il numero di giorni: ")) *24 * 3600
    ore = int(input("Inserisci il numero di ore: ")) * 3600
    minuti = int(input("Inserisci il numero di minuti: ")) * 60
    print(f"Il numero complessivo in secondi è : {giorni + ore + minuti}s")

def americanConverter():
    metri = float(input("Fornisci in input un valore in metri: "))
    miglia = metri / 1609.344
    piedi = metri * 3.280840
    pollici = metri * 3.280840
    iarde = metri * 1.093613
    print(f'''
    {metri} metri in miglia sono {miglia}
    {metri} metri in piedi sono {piedi}
    {metri} metri in pollici sono {pollici}
    {metri} metri in iarde sono {iarde}

    ''')