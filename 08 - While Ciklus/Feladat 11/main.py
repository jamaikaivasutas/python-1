from os import system
import random

paros : int = None
paratlan : int = None
temp : str = None
veletlen : int = None
atlag: int = None
oszthato: int = 0

system('cls')

while(paros == None):
    print("Kérek egy páros számot!")
    temp = int(input())
    if(temp % 2 == 0 ):
        paros=temp
    else:
        print("Nem páros számot adott meg!")

while(paratlan == None):
    print("Kérek egy nagyobb páratlan számot!")
    temp = int(input())
    if(temp % 2 == 1 and temp > paros):
        paratlan=temp
    elif(temp <= paros):
        print("Nem nagyobb számot adott meg!")
    else:
        print("Nem páratlan számot adott meg!")

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