import numbers
from os import *

number1: float = None
number2: float = None
number3: float = None
solution: float = None

system('cls')

print("Kérek egy számot!")
number1=float(input())

print("Kérek egy másik számot!")
number2=float(input())

print("Kérek egy másik számot!")
number3=float(input())

solution=((number1+0.5)*(number2-0.7))%number3

print(f"Az eredmény: {solution}")