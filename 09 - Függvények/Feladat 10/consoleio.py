import random

def genRnd(start:int, end:int)->int:
    ran: int = None
    ran=random.randint(start,end)
    return ran

def guess(number:int)->int:
    guess: int = None
    trial: int = 0
    while(guess != number):
        trial=trial+1
        guess=genRnd(0, 50)
        if(guess > number):
            print("A kitalálandó szám kisebb.")
        elif(guess == number):
            print("Eltalálta a számot!")
        else:
            print("A kitalálandó szám nagyobb")
    return trial

