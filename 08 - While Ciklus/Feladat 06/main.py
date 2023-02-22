from os import system

temp: str = None
truncatedString: str = None
isNumber: bool = None
age: int = 0

while(age >= 99 or age <= 0):
    print("Hány éves?")
    temp = str(input())
    truncatedString = temp.replace(" ", "").replace(".", "")
    isNumber=truncatedString.isnumeric()
    if(isNumber):
        age = int(temp)
        if(age >= 99 or age <= 0):
            print("Nem jóú, adjon meg másikat!")
    else:
        print("Hát ez nem a korood.")

if(age <= 6):
    print("gyerek")
elif(age <= 18):
    print("iskolás")
elif(age <= 65):
    print("dolgozó")
else:
    print("nyugdíjas")