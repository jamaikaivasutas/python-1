from inspect import istraceback
from os import system

system('cls')

border: int = 0
number: int = None
isNumber: bool = False
temp: str= None
truncatedString: str = None
sum: int = 0

while(border <= 100):
    print("Kérem a határértéket!")
    temp = str(input())
    truncatedString = temp.replace(" ", "").replace(".", "")
    isNumber = truncatedString.isnumeric()
    if(isNumber):
        border = int(temp)
        if(border <= 100):
            print("Nagyobb számot adjon meg mint száz!")
    else:
        print("Nem számot adott meg.")
    
isNumber=False

while(sum <= border):
    print("Kérek egy számot!")
    temp = str(input())
    truncatedString = temp.replace(" ", "").replace(".", "")
    isNumber = truncatedString.isnumeric()
    if(isNumber):
        number=int(temp)
        sum = sum + number
        print(f"A jelenlegi összeg: {sum}")
    else:
        print("Nem számot adott meg!")
    
print("Az összeg meghaladta a határértéket!")