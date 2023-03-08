def getNumber()->float:
    number: float = None
    temp: str = None
    truncatedString: str = None
    isNumber: bool = False

    while(number == None):
        print("Kérek egy számot!")
        temp = input()
        truncatedString = temp.replace("-","")
        isNumber = truncatedString.isnumeric()
        if(isNumber):
            number = float(temp)
        else:
            print("Nem számot adott meg!")

    return number

def printConsole(a:float, b:float, operator:str, eredmeny:float)->float:
    print(f"{a}{operator}{b}={eredmeny}")