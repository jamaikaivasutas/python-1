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

def printConsole(name):
    print(f"Üdvözöljük {name}!")
    
