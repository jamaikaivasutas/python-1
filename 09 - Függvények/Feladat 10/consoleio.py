import random

def genRnd(start:int, end:int)->int:
    ran: int = None
    ran=random.randint(start,end)
    return ran

def guess(number1:int, number2:int, number3:int)->int:
    guess: int = None
    trial: int = 0
    while(guess != number3):
        trial=trial+1
        guess=genRnd(number1, number2)
        if(guess > number3):
            print("A kitalálandó szám kisebb.")
            number2=guess
        elif(guess == number3):
            print("Eltalálta a számot!")
        else:
            print("A kitalálandó szám nagyobb")
            number1=guess
    return trial

