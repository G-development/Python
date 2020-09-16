def rimario(lista,parola):
    rime = []
    for elemento in lista:
        if parola[-3:] == elemento[-3:]:
            rime.append(elemento)

    if not rime:
            print(f"Non sono state trovate rime con '{parola}'")
    else:
            print(f"Le rime trovate con '{parola}' sono {rime}")

def crittografiaROT13():
    cifrario = {'a':'n', 'b':'o', 'c':'p', 'd':'q', 'e':'r', 'f':'s', 'g':'t', 'h':'u',
                'i':'v', 'j':'w', 'k':'x', 'l':'y', 'm':'z', 'n':'a', 'o':'b', 'p':'c',
                'q':'d', 'r':'e', 's':'f', 't':'g', 'u':'h', 'v':'i', 'w':'j', 'x':'k',
                'y':'l', 'z':'m', 'A':'N', 'B':'O', 'C':'P', 'D':'Q', 'E':'R', 'F':'S',
                'G':'T', 'H':'U', 'I':'V', 'J':'W', 'K':'X', 'L':'Y', 'M':'Z', 'N':'A',
                'O':'B', 'P':'C', 'Q':'D', 'R':'E', 'S':'F', 'T':'G', 'U':'H', 'V':'I',
                'W':'J', 'X':'K', 'Y':'L', 'Z':'M'}
    
    scelta = int(input('''
    Crittografia ROT13
    1- Codifica una parola
    2- Decodifica una parola
    3- Exit
    '''))

    if scelta == 1:
        print("Hai scelto Codifica una parola:")
        msg = input("Inserisci la parola da codificare: ")

        msgCodificato = ""
        for carattere in msg:
            if carattere in cifrario:
                msgCodificato += cifrario[carattere]
            else:
                msgCodificato += carattere

        print(msgCodificato)

    if scelta == 2:
        print("Hai scelto Decodifica una parola:")
        msg = input("Inserisci il messaggio da decodificare: ")

        msgInChiaro = ""
        for carattere in msg:
            if carattere in cifrario:
                msgInChiaro += cifrario[carattere]
            else: msgInChiaro += carattere

        print (msgInChiaro)

    
    if scelta == 3:
        exit