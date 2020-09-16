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