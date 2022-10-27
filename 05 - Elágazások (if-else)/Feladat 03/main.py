from os import *

number: int = None

system('cls')

print("Kérek egy számot!")
number = int(input())

if(number > -30 and number < 40):
    print("A szám 40 és -30 között van.")
else:
    print("A szám nincs 40 és -30 között.")