from os import system
from select import KQ_NOTE_WRITE

zoldLeves: bool=False
husLeves: bool=False
gyumLeves: bool=False

sultCsirkeComb: bool=False
sultCsirkemell: bool=False
rakottZold: bool=False
spagetti: bool=False
pizza: bool=False

rizs: bool=False
paroltZold: bool=False
gyumolcs: bool=False
sultKrumpli: bool=False
salata: bool=False
kola: bool=False

valasztas: int = None

eloetel: bool = False
foetel: bool = False
koret: bool = False

print("Kérem jelezze a menüben szereplő ételeket/köreteket!")
print("Zöldségleves [1]:")
print("Húsleves [2]:")
print("Gyümölcsleves [3]:")

valasztas = int(input())

if(valasztas == 1):
    zoldLeves=True
elif(valasztas == 2):
    husLeves=True
elif(valasztas == 3):
    gyumLeves=True

print("Sültcsirkecomb [1]:")
print("Sültcsirkemell [2]:")
print("Rakottzöldség [3]:")
print("Spagetti [4]:")
print("Pizza [5]:")

valasztas = int(input())

if(valasztas == 1):
    sultCsirkeComb=True
elif(valasztas == 2):
    sultCsirkemell=True
elif(valasztas == 3):
    rakottZold=True
elif(valasztas == 4):
    spagetti=True
elif(valasztas == 5):
    pizza=True

print("Rizs [1]:")
print("Pároltzöldség [2]:")
print("Gyümölcs [3]:")
print("Sültkrumpli [4]:")
print("Saláta [5]:")
print("Kóla [6]:")

valasztas = int(input())

if(valasztas == 1):
    rizs=True
elif(valasztas == 2):
    paroltZold=True
elif(valasztas == 3):
    gyumolcs=True
elif(valasztas == 4):
    sultKrumpli=True
elif(valasztas == 5):
    salata=True
elif(valasztas == 6):
    kola=True

eloetel = zoldLeves or husLeves or gyumLeves
foetel = sultCsirkeComb or sultCsirkemell or rakottZold or spagetti or pizza
koret = rizs or paroltZold or gyumolcs or sultKrumpli or salata or kola

if(eloetel and foetel and koret):
    if((zoldLeves or spagetti or gyumolcs or salata) and not (pizza or sultKrumpli)):
        print("Kíváló értékelés.")




