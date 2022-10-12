from os import system

releaseDate: int=None
directorName: str=None
movieName: str=None
mainCharacter: str=None

print("Kérem a film megjelenési évét!")
releaseDate=int(input())

print("Kérem a film forgatójának a nevét!")
directorName=str(input())

print("Kérem a film címét!")
movieName=str(input())

print("Kérem a film főszereplőjének a nevét!")
mainCharacter=str(input())

system('cls')

print(f"{releaseDate}-ban {directorName} rendezésében megjelent a/az {movieName} című film {mainCharacter} főszereplésével!")