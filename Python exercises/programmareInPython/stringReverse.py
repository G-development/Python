def stringReverser():
    stringa = input("Inserisci una stringa: ")
    index = (len(stringa)-1)
    stringaNuova = ""
    while index >= 0:
        stringaNuova += stringa[index]
        index -= 1

    print(stringaNuova)