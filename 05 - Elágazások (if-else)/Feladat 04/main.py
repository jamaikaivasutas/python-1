from os import *

number1: int = None
number2: int = None

system('cls')

print("Kérek egy számot!")
number1 = int(input())

print("Kérek egy másik számot!")
number2 = int(input())

if(number1 > number2):
    print(f"{number1}")
else:
    print(f"{number2}")