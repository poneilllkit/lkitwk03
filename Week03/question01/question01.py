import random

num = random.randint(1, 10)
guess = None

while guess != num:
    guess = input("guess a number between 1 and 10: ")
    guess = int(guess)

    if guess == num:
        print("well done! you guessed right. ")
        break
    else:
        print("whoops, that's not it. try again!")