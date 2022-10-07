from os import system

name: str=None
birthDate: int=None

print("Adja meg a nevét!")
name = str(input())

print("Adja meg a születési évét!")
birthDate = int(input())

system('cls')

print(f"{name} ön {birthDate} született!")