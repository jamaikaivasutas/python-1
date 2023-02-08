from os import system
from sysconfig import parse_config_h
from tokenize import single_quoted

paros : int = None
paratlan : int = None
temp : str = None

system('cls')

while(paros == None):
    print("Kérek egy páros számot!")
    temp = int(input())
    if(temp % 2 == 0 ):
        paros=temp
    else:
        print("Nem páros számot adott meg!")

while(paratlan == None):
    print("Kérek egy nagyobb páratlan számot!")
    temp = int(input())
    if(temp % 2 == 1 and temp > paros):
        paratlan=temp
    elif(temp <= paros):
        print("Nem nagyobb számot adott meg!")
    else:
        print("Nem páratlan számot adott meg!")