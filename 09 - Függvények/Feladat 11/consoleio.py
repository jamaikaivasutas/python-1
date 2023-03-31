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
    
def getWork()->int:
    work: int = None
    temp: str = None
    truncatedString: str = None
    isNumber: bool = True

    while(work == None):
        print("Kérem a ledolgozott órák számát!")
        temp = str(input())
        truncatedString = temp.replace("-", "").replace(" ", "")
        isNumber = truncatedString.isnumeric()
        if(isNumber and int(truncatedString)<=70):
            work = int(truncatedString)
            return work
        else:
            print("Ez nem az órák száma!")

def earn(work:int)->int:
    earnings: int = None
    extraWork: int = None
    normalWork: int = None

    extraWork=work-40
    normalWork=work-extraWork

    earnings=normalWork*1000+extraWork*1500

    return earnings
    
def printConsole(name1:str, name2:str, name3:str, name4:str, name5:str, work1:int, work2:int, work3:int, work4:int, work5:int, earning1:int, earning2:int, earning3:int, earning4:int, earning5:int):
    print(f"A ledolgozott órákért kapott munkabér:\n{name1}: {work1} ledolgozott óra, kereset: {earning1} HUF\n{name2}: {work2} ledolgozott óra, kereset: {earning2} HUF\n{name3}: {work3} ledolgozott óra, kereset: {earning3} HUF\n{name4}: {work4} ledolgozott óra, kereset: {earning4} HUF\n{name5}: {work5} ledolgozott óra, kereset: {earning5} HUF\n")