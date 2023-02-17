from os import system

system('cls')

number: int = None
sum: int = 0
isNumber: bool = False
temp: str = None
truncatedString: str = None

while(sum <= 100):
    print("Kérek egy számot!")
    temp = str(input())
    truncatedString=temp.replace(" ", "").replace(".", "")
    isNumber=truncatedString.isnumeric()
    if(isNumber):
        number=int(temp)
        sum= sum + number
        print(f"A jelenlegi összeg: {sum}")
    else:
        print("Nem számot adott meg!")

print("Az összeg meghaladta a százat!")