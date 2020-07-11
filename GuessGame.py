import random

Gamer_Over = False
Guess = 1

NumberToGuess = random.randint(1,100)

number = int(input("Enter a number between 1 to 100: "))

while not Gamer_Over :
    if number == NumberToGuess:
        print(f"You Win, You Guessed in {Guess} Times")
        Gamer_Over = True
    else:
        if number < NumberToGuess:
            print("Low")
        else:
            print("High")
        Guess += 1
        number = int(input("Guess Agian: "))