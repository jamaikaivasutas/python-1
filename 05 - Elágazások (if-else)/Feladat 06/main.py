from os import *

number1:int=None
number2:int=None
number3:int=None

system('cls')

print("Kérek egy számot!")
number1=int(input())

print("Kérek egy másik számot!")
number2=int(input())

print("Kérek egy másik számot!")
number3=int(input())

if(number1 > number2 and number2 > number3):
    print(f"{number3}, {number2}, {number1}")
elif(number1 > number3 and number3 > number2):
    print(f"{number2}, {number3}, {number1}")
elif(number2 > number1 and number1 > number3):
    print(f"{number3}, {number1}, {number2}")
elif(number2 > number3 and number3 > number1):
    print(f"{number1}, {number3}, {number2}")
elif(number3 > number2 and number2 > number1):
    print(f"{number1}, {number2}, {number3}")
elif(number2 > number1 and number1 > number3):
    print(f"{number1}, {number3}, {number2}")