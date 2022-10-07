from socket import NI_NAMEREQD


from os import system

name: str=None
key: str=None

print("Adja meg a nevét!")
name=str(input())

print("Nyomjon meg egy gombot a billentyűzeten!")
key=str(input())

system('cls')

print(f"{name} ön a/az {key} billentyűt nyomta meg!")