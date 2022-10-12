from os import system
from platform import release

brand: str=None
model: str=None
type: str=None
cubicCentimeters: int=None
releaseDate: int=None

print("Kérem a kedvenc autójának a márkáját!")
brand=str(input())

print("Kérem a kedvenc márkájának a modeljét!")
model=str(input())

print("Kérem a kedvenc autójának a típusát!")
type=str(input())

print("Kérem a kedvenc autójának a köbcentijét!")
cubicCentimeters=int(input())

print("Kérem a kedvenc autójának a megjelenési évét!")
releaseDate=int(input())

system('cls')

print(f"Márka: {brand}\nModell: {model}\nTípus: {type}\nKöbcenti: {cubicCentimeters}\nMegjelenési év: {releaseDate}")