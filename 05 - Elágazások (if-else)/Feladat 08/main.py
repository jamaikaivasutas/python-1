from os import *

number:int=None

system('cls')

print("Kérek egy számot!")
number=int(input())

if(number % 4 == 0 and number % 6 == 0):
    print(f"A szám ({number}) osztható 4-el és 6-al.")
else:
    print("A szám nem osztható 4-el és 6-al.")