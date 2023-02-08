from os import system

number : int = None
temp : str = None

system('cls')

while(number == None):
    print("Kérek egy háromjegyű számot!")
    temp = str(input())
    if(len(temp) == 3):
        number=int(temp)
    else:
        print("Nem háromjegyű számot adott meg.")

if(number % 7 == 0):
    print("A szám oszható héttel.")
else:
    print("A szám nem osztható héttel.")