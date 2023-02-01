from os import system

age: int = 0

while(age >= 99 or age <= 0):
    print("Hány éves?")
    age = int(input())
    if(age >= 99 or age <= 0):
        print("Nem jó, adjon meg másikat!")

