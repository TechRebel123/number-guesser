import random

number = random.randint(1, 100)

player_guess=0

while player_guess != number:

    guess = int(input("Guess The Number:"))

    if guess > number:
        print("Guess Lower!")
    elif guess < number:
        print("Guess Higher")
    else:
        print("You Win!")
        break