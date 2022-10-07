from os import system

name: str=None
height: int=None

print("Adja meg a nevét!")
name=str(input())

print("Adja meg a magasságát (centiméterben)!")
height=int(input())

system('cls')

print(f"{name} az ön magassága {height} cm")