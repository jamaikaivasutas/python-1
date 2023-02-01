name: str = None
isName: bool = False

while(isName == False):
    print("Kérem a nevét!")
    name = str(input())
    if(len(name) >= 2):
        isName = True
    else:
        print("Nem nevet adott meg.")