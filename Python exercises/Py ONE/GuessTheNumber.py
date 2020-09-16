import random

num = random.randint(0,20)
user = int(input("\nGuess the number between 0-20: "))

moves = 0
while user != num:
    if user<num:
        print("The number is bigger!")
        user = int(input("Retry: "))
        moves += 1
    else: 
        print("The number is smaller!")
        user = int(input("Retry: "))
        moves += 1

print("Found it in:", moves, "moves.")