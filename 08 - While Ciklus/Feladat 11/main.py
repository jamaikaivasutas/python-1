from os import system
import random

paros : int = None
paratlan : int = None
temp : str = None
truncatedString : str = None
isNumber : bool = False
veletlen : int = None
atlag: int = None
oszthato: int = 0

system('cls')

while(paros == None):
    print("Kérek egy páros számot!")
    temp = str(input())
    truncatedString = temp.replace(" ", "").replace(".", "")
    isNumber=truncatedString.isnumeric()
    if(isNumber and int(temp) % 2 == 0):
        paros=int(temp)
    else:
        print("Nem jó számot adott meg!")

isNumber = False

while(paratlan == None):
    print("Kérek egy nagyobb páratlan számot!")
    temp = str(input())
    truncatedString = temp.replace(" ", "").replace(".", "")
    isNumber=truncatedString.isnumeric()
    if(isNumber and (int(temp) % 2 == 1 and int(temp) > paros)):
        paratlan=int(temp)
    else:
        print("Nem jóú")

veletlen = random.randint(paros, paratlan)

for i in range(paros, paratlan + 1, 1):
    if(i % 4 == 0):
        oszthato = oszthato + 1

atlag=(paros+paratlan)/2
if(veletlen>atlag):
    print(f"A véletlen szám a páratlan számhoz van közelebb, a szám: {veletlen}")
else:
    print(f"A véletlen szám a páros számhoz van közelebb, a szám: {veletlen}")
print(f"A két szám közti átlag {atlag}")
print(f"A néggyel osztható számok száma: {oszthato}")