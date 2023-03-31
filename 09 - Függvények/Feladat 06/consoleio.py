def getParam()->str:
    parameter: str = None
    temp: str = None

    while(parameter == None):
        print("Válaszza ki a megfelelő paramétert!\n[F, Farrenheit] [K, kelvin]")
        temp = input()
        if(len(temp)==1):
            parameter = temp
        else:
            print("Nem paramétert adott meg!")

    return parameter

def getTemp()->float:
    temperature: float = None
    temp: str = None
    truncatedString: str = None
    isNumber: bool = False

    while(temperature == None):
        print("Adjon meg egy hőmérsékletet celsius fokban!")
        temp = input()
        truncatedString = temp.replace("-","")
        isNumber = truncatedString.isnumeric()
        if(isNumber):
            temperature = float(temp)
        else:
            print("Nem számot adott meg!")

    return temperature


def atalakit(celsius: float, parameter: str)->float:
    kelvin: float = None
    farrenheit: float = None
    if(parameter == "F" or parameter == "f"):
        farrenheit = 9/5*celsius+32
        return farrenheit
    elif(parameter == "K" or parameter == "k"):
        kelvin = 273+celsius
        return kelvin

def printConsole(eredmeny, parameter):
    print(f"Az átváltott érték: {eredmeny} {parameter}")