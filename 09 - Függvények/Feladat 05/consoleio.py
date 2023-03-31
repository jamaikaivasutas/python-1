from operator import truediv


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
def sameChar(str1:str, str2:str)->int:
    same: bool = False
    charNum: int = 0

    for char in str1:
        print(char)
        if not char in str2:
            same=False
        same=True
        if(same):
            charNum=charNum+1
    return charNum

