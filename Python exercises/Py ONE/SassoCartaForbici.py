import random

print("Sasso Carta Forbici\nLet's Play\n")
print("1- Sasso\n2- Carta\n3- Forbici\n")


playerChoice = input("Make your choice:")
pcChoice = random.randint(1,3)

# Assign the number to the coice for player
if playerChoice == "1": playerChoice = "s"
elif playerChoice == "2": playerChoice = "c"
else: playerChoice = "f"
# Assign the number to the coice for pc
if pcChoice == 1: pcChoice = "s"
elif pcChoice == 2: pcChoice = "c"
else: pcChoice = "f"

# Check the choices
if playerChoice == pcChoice:
    print("Parità!")
elif playerChoice=="s" and pcChoice=="f" or playerChoice=="f" and pcChoice=="c" or playerChoice=="c" and pcChoice=="s":
    print("You won!")
else: print("You lose!")
 
    
print(playerChoice)
print(pcChoice)
