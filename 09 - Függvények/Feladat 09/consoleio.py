def getNum()->float:
    temp: str=None
    truncatedString: str=None
    isNumber: bool=False
    number: float=None
    
    temp=str(input())
    truncatedString=temp.replace(" ", "")
    isNumber=truncatedString.isnumeric
    
    if(isNumber):
        number=float(truncatedString)
        return number
    else:
        print("Nem számot adott meg!")

def convEUR(number:float)->float:
    EUR=number/380
    return EUR

def convJPY(EUR:float)->float:
    JPY=EUR*0.75
    return JPY

def convUSD(EUR:float)->float:
    USD=EUR*0.8
    return USD

def convCHF(EUR:float)->float:
    CHF=EUR*0.75
    return CHF

def printConsole(EUR:float, number:float, type:str):
    print(f"Az átváltott forint, {EUR} Euró, {number} {type}.")