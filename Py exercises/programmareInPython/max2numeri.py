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