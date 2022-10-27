from os import *

number:int=None

system('cls')

print("Kérek egy számot!")
number=int(input())

system('cls')

if(number > 0):
    if(number % 2 == 0):
        if(number % 5 == 0):
            print("A szám páros, pozitív, 5-el osztható.")
        else:
            print("A szám páros, pozitív, nem osztható 5-el.")
elif(number % 3 == 0):
    print(f"BAZ")
elif(number % 2 == 0):
    print(f"BIZ")
else:
    print(f"A szám nem osztható se 2-vel,3-al se.")