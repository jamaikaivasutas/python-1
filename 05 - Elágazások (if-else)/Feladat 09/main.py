from os import *

numberX:int=None
numberY:int=None

system('cls')

print("Kérek egy számot!")
numberX=int(input())

print("Kérek egy számot!")
numberY=int(input())

if(numberX % numberY == 0):
    print(f"A {numberX} osztható {numberY}.")
else:
    print(f"A szám nem osztható {numberY}.")