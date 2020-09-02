#https://www.programmareinpython.it/esercizi-python/
import random
import platform #in pcInfos
import os #in folderWeight
import smtplib #in postino

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
    psw = ""

    sceltaPSW = input('''
    Password generator:
    1- Password semplice? (8 caratteri)
    2- Password difficile? (20 caratteri)
    3- Scegli lunghezza password
    4- Esci
    ''')

    if int(sceltaPSW) == 1:
        print("Hai scelto password semplice: ")
        for x in range(8):
            psw += alpha_char_table[int(random.randrange(len(alpha_char_table)))]
            x += 1
        print("La password è " + psw)

    if int(sceltaPSW) == 2:
        print("Hai scelto password difficile: ")
        for x in range(20):
            psw += full_char_table[int(random.randrange(len(full_char_table)))]
            x += 1
        print("La password è " + psw)
    
    if int(sceltaPSW) == 3:
        pswLength = input("Inserisci lunghezza password: ")
        for x in range(int(pswLength)):
            psw += full_char_table[int(random.randrange(len(full_char_table)))]
            x += 1
        print("La password è " + psw)

    if int(sceltaPSW) == 4:
        print("Goodbye!")
        exit

    else: 
        passwordGenerator()

def fattoriale(num):
    #iterativa, forumula n(n-1)/2
    if num == 1:
        return num
    else:
        res = num * fattoriale(num-1)
        return res

def fibonacci(num):
    #iterativa, n1=1, n2=2 -> n3= n1+n2
    if num <= 1:
        return num
    else:
        return fibonacci(num-1) + fibonacci(num-2)

def generateMAC():
    alpha_char = "0123456789ABCDEF"
    MAC = ""

    for x in range (6):
        for x in range (2):
            MAC += alpha_char[int(random.randrange(len(alpha_char)))]
        MAC += " : "
    print("L'indirizzo MAC generato è: " + MAC)

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

def pcInfos():
    print("Il tuo sistema operativo è " + platform.system())
    print("La release è " + platform.release())
    print(f"L'architettura è {platform.architecture()}")

def whatAscii():
    char = input("Inserisci un carattere: ")
    print (f"Il carattere '{char}' in codice ASCII è '{ord(char)}'")

def folderWeight():
    tot = 0
    folder = os.getcwd()
    for file in os.listdir(folder):
        tot += os.path.getsize(os.path.join(folder, file))
    print (f"La somma delle dimensioni dei file nella directory è: {tot/1048576}MB")

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

def postino():
    print('''
    Questa è la funzione Postino: spedisce eMail utilizzando Gmail!
    Server: smtp.gmail.com
    Porta: 587
    Si richiedono: Username, Password, Destinatario, Oggetto e Messaggio da inviare.
    ''')

    username = input("Inserisci il tuo username: ")
    password = input("Inserisci la tua password: ")
    destinatario = input("Inserisci l'email del destinatario: ")
    oggetto = input("Inserisci l'oggetto della mail: ")
    messaggio = input("Ora puoi inserire il messaggio che vuoi inviare: ")
    contenuto = f"Subject: {oggetto}\n\n{messaggio}"
    print("Sto effettuando la connessione col Server...")
    email = smtplib.SMTP("smtp.gmail.com",587)
    email.ehlo()
    email.starttls()
    email.login(username,password)
    print("Sto inviando...")
    email.sendmail(username, destinatario, contenuto)
    email.quit()
    print("Messaggio Inviato!")


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
    #lista = ["ciao", "due", "liao", "viao"]
    #parola = "ciao"
    #rimario(lista, parola)
    #listaParole = ["ciao", "come", "stai"]
    #aCiascunoIlSuo(listaParole)
    #libreria = {"libro1": 10 , "libro2": 22 , "libro3": 1}
    #ordini = []
    #libro = "libro4"
    #sellBooks(libreria, libro)

    #stringReverser()
    #checkPalindromo()
    #linguaggioFurfanti()
    #frequenzimetro()
    #geometra()
    #passwordGenerator()
    #generateMAC()
    #crittografiaROT13()
    #timeMaster()
    #americanConverter()
    #pcInfos()
    #whatAscii()
    #folderWeight()

    #iterative
    #num = int(input("Inserisci numero:"))
    #print(fattoriale(num))
    #limite = int(input("Inserisci quanti valori vuoi avere: "))
    #for num in range(1, limite+1):
    #    print(fibonacci(num))

    postino()


if __name__ == "__main__":
    main()
    