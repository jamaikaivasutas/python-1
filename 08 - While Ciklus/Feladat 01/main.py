number: float = None
isNumber: bool = False
temp: str = None
truncatedString: str = None

while(number == None or (number < 0 or number > 9)):
    print("Adjon meg egy számot: ", end="")
    temp = input()
    truncatedString = temp.replace(".","").replace("-","")
    isNumber = truncatedString.isnumeric()

    if(isNumber):
        number = float(temp)
    else:
        print("Nem számot adott meg")
