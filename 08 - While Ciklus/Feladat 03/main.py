import random

number: int = random.randint(0, 9)
guess: int = None
trial: int = 0
temp: str = None
isNumber: bool = False
truncatedString: str = None



while(number != guess and trial <= 5):
    print("Találja ki a számot! Kérek egy számot!")
    temp=str(input())
    truncatedString=temp.replace(" ", "").replace(".", "")
    isNumber=truncatedString.isnumeric()
    if(isNumber):
        number=int(temp)
        trial=trial+1
    else:
        print("Nem számot adott meg!")

if(guess == number):
    print("Eltalálta a számot!")
else:
    print("Nem talált!")
