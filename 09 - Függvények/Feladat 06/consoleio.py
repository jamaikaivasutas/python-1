def atalakit(celsius: float, parameter: str)->float:
    kelvin: float = None
    farrenheit: float = None
    if(parameter == "F"):
        farrenheit = 9/5*celsius+32
        return farrenheit
    elif(parameter == "K"):
        kelvin = 273+celsius
        return kelvin

def printConsole(eredmeny, parameter):
    print(f"Az átváltott érték: {eredmeny} {parameter}")