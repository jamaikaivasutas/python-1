from os import system

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



