from os import *

number: int = None

system('cls')

print("Kérek egy számot!")
number = int(input())

if(number > 0):
    print(f"A szám nagyobb a nullánál, ez a szám: {number}.")
else:
    print("A szám kisebb nullánál.")