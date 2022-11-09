from os import system

number: int=None

system('cls')

print("Kérek egy számot!")
number=int(input())

if(0<=number and 9>=number):
    print("A szám egyjegyű.")
if(10<=number and 99>=number):
    print("A szám kétjegyű.")
if(100<=number and 999>=number):
    print("A szám háromjegyű.")