from os import system

system('cls')

number: int = 0
temp: str = None
truncatedString: str = None

print("Coca Cola [1]\nPepsi [2]\nFanta [3]\nSprite [4]\nÁsványvíz [5]")

while(number == None or number > 5 or number < 1):
    print("Kérek egy számot a menüből!")
    temp = input()
    truncatedString = temp.replace(".","").replace("-","")
    isNumber = truncatedString.isnumeric()

    if(isNumber):
        number = int(temp)
    else:
        print("Nem számot adott meg!")
    if((number < 1 or number > 5) and isNumber):
        print("Ilyen nincs a menüben!")
    
match(number):
    case 1:
        print("A Coca Cola üdítő kilett adva.")
    case 2:
        print("A Pepsi üdítő kilett adva.")
    case 3:
        print("A Fanta üdítő kilett adva.")
    case 4:
        print("A Sprite üdítő kilett adva.")
    case 5:
        print("Az ásványvíz kilett adva.")
    