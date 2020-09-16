#Write a Python program which accepts the radius of a circle from the user and compute the area.
#Circle area = Pi r^2

import math

r = float(input("Inserisci raggio: "))
print("L'area è: " + str(math.pi * r**2))