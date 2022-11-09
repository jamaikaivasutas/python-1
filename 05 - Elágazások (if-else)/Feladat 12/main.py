from os import system

number: int=None

system('cls')

print("Kérek egy számot!")
number=int(input())

if(10<number and number<20):
    print("A szám 10 és 20 között van.")
if(-20<number and number<-10):
    print("A szám -20 és -10 között van.")
else:
    print("A szám nincs 10 és 20 között és -10 és -20 között.")