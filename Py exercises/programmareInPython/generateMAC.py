def generateMAC():
    alpha_char = "0123456789ABCDEF"
    MAC = ""

    for x in range (6):
        for x in range (2):
            MAC += alpha_char[int(random.randrange(len(alpha_char)))]
        MAC += " : "
    print("L'indirizzo MAC generato è: " + MAC)