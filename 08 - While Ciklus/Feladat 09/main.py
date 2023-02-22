from argparse import ONE_OR_MORE
from os import system

number : int = None
temp : str = None
truncatedString: str = None
isNumber: bool = None

system('cls')

while(number == None):
    print("Kérek egy háromjegyű számot!")
    temp = str(input())
    truncatedString = temp.replace(".", "").replace(" ", "").replace("-", "")
    isNumber = truncatedString.isnumeric()
    if(isNumber and len(truncatedString) == 3):
        number=int(temp)
    else:
        print("Nem háromjegyű számot adott meg.")

if(number % 7 == 0):
    print("A szám oszható héttel.")
else:
    print("A szám nem osztható héttel.")