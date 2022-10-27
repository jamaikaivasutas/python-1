from os import *

number:int=None

system('cls')

print("Kérek egy számot!")
number=int(input())

system('cls')

if(number % 3 == 0 and number % 2 == 0):
    print(f"ZIZI")
elif(number % 3 == 0):
    print(f"BAZ")
elif(number % 2 == 0):
    print(f"BIZ")
else:
    print(f"A szám nem osztható se 2-vel,3-al se.")