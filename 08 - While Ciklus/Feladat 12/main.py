from os import system

temp: str = None
truncatedString: str = None
isNumber: bool = False
mPenz: int = None
osszeg: int = None
honap: int = 0

system('cls')

while(mPenz == None):
    print("Mennyi megtakarított pénze van?")
    temp=str(input())
    truncatedString=temp.replace(" Ft", "")
    isNumber=truncatedString.isnumeric()
    if(isNumber and int(truncatedString) < 100000):
        mPenz = int(temp)
    else:
        print("Nem jó értéket adott meg!")
    


while(mPenz < 100000):
    mPenz = mPenz * 1.02
    honap = honap + 1

print(f"{honap} hónap múlva éri el a 100000 Ft-ot.")

