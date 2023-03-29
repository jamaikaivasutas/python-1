def getText()->str:
    text: str = None
    temp: str = None
    isText: bool = False

    while(isText == False):
        print("Adjon meg egy szöveget!")
        temp = str(input())
        if(2 <= len(temp)):
            text = temp
            isText = True
            return text
        else:
            print("Nem szöveget adott meg.")



