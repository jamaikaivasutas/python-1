number: float = None
isNumber: bool = False
temp: str = None

while(number == None or (number < 0 or number > 9)):
    print("Adjon meg egy számot: ", end="")
    temp = input()
    isNumber = isinstance(temp, (int, float))

    if(isNumber):
        number = float(temp)
    else:
        print("Nem számot adott meg")
