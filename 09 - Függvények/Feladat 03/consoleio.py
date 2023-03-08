def getName()->str:
    name: str = None
    temp: str = None
    isName: bool = False

    while(isName == False):
        print("Adja meg a nevét!")
        temp = str(input())
        if(2 <= len(temp)):
            name = temp
            isName = True
            return name
        else:
            print("Nem nevet adott meg.")

def getAge()->int:
    age: int = None
    temp: str = None
    truncatedString: str = None
    isNumber: bool = True

    while(age == None):
        print("Kérem a korát!")
        temp = str(input())
        truncatedString = temp.replace("-", "").replace(" ", "")
        isNumber = truncatedString.isnumeric()
        if(isNumber):
            age = int(temp)
            return age
        else:
            print("Ez nem a kora!")

def printName(name, age)->str:
    print(f"{name} ön az idén {age} éves!")