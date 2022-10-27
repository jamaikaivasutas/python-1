from os import *

number:int=None

system('cls')

print("Kérek egy számot!")
number=int(input())

if(number % 5 == 0):
    print(f"A szám ({number}) osztható 5-el.")
else:
    print("A szám nem osztható 5-el.")