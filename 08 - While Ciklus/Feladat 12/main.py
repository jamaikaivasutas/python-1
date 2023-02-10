from os import system

temp: int = None
mPenz: int = None
osszeg: int = None
honap: int = 0

system('cls')

while(mPenz == None):
    print("Mennyi megtakarított pénze van?")
    temp=str(input())
    temp=temp.replace(" Ft", "")
    if(int(temp) < 100000):
        mPenz = int(temp)
    else:
        print("Kisebb értéket adjon meg mint 100000 Ft.")
    


while(mPenz < 100000):
    mPenz = mPenz * 1.02
    honap = honap + 1

print(f"{honap} hónap múlva éri el a 100000 Ft-ot.")

