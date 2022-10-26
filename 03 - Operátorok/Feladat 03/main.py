from os import system

number1: int=None
number2: int=None
number3: int=None
solution: int=None

system('cls')

print("Kérek egy számot!")
number1=int(input())

print("Kérek egy másik számot!")
number2=int(input())

print("Kérek egy másik számot!")
number3=int(input())

solution=(number1-number2)*number3

print(f"Az eredmény:{solution}")