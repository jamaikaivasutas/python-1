from os import *

number: int = None

system('cls')

print("Kérek egy számot!")
number = int(input())

if(number >= 0):
    print("pozitiv")
else:
    print("negativ")