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
    hossz: int = None
    
    hossz=len(name)
    match hossz:
        case 2:
            print(f"\033[1;30m Üdvözöljük {name}\n")
        case 2:
            print(f"\033[1;31m Üdvözöljük {name}\n")
        case 3:
            print(f"\033[1;32m Üdvözöljük {name}\n")
        case 4:
            print(f"\033[1;33m Üdvözöljük {name}\n")
        case 5:
            print(f"\033[1;34m Üdvözöljük {name}\n")
        case 6:
            print(f"\033[1;35m Üdvözöljük {name}\n")
        case 7:
            print(f"\033[1;36m Üdvözöljük {name}\n")
        case 8:
            print(f"\033[1;37m Üdvözöljük {name}\n")
        case _: 
            print(f"Üdvözöljük {name}")
    

