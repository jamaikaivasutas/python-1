from os import system

age: int = 0

while(age >= 99 or age <= 0):
    print("Hány éves?")
    age = int(input())
    if(age >= 99 or age <= 0):
        print("Nem jó, adjon meg másikat!")

if(age <= 6):
    print("gyerek")
elif(age <= 18):
    print("iskolás")
elif(age <= 65):
    print("dolgozó")
else:
    print("nyugdíjas")