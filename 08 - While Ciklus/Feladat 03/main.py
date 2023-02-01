import random

number: int = random.randint(0, 9)
guess: int = None
trial: int = 0

while(number != guess and trial <= 5):
    trial=trial+1
    print("Találja ki a számot! Kérek egy számot!")
    guess=int(input())
    if(guess == number):
        print("Eltalálta a számot!")
    else:
        print("Nem talált!")
