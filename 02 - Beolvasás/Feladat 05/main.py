from os import system

bandName: str=None
songName: str=None
songLength: float=None

print("Kérem a kedvenc együttesének a nevét!")
bandName=str(input())

print("Kérem a kedvenc zenédnek a címét!")
songName=str(input())

print("Kérem a kedvenc dalának a hosszát!")
songLength=str(input())

system('cls')

print(f"Az ön kedvenc együttesének {bandName} a legjobb zeneszáma {songName} melynek hossza {songLength} perc!")