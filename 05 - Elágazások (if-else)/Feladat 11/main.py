from os import system

number: int=None

system('cls')

print("Kérek egy számot")
number=int(input())

if(number % 2 == 0):
    print("A szám páros.")
else:
    print("A szám páratlan.")

if(number >= 0):
    print("A szám pozitív.")
else:
    print("A szám negatív.")
    
if(number% 5 == 0):
    print("A szám osztható öttel.")
else: 
    print("A szám nem osztható öttel.")