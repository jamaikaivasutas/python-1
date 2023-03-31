from consoleio import *
from os import system

system('cls')

money: int=None
EUR: float=None
convValue: float=None
choice: int=None

print("Adja meg, mennyi pénzt szeretne átváltani!")
money=getNum()

print("Válasszon az alábbi menüből, mibe szerente átváltani:\n[1] Japán jen\n[2] Dollár\n[3] Svájci frank")
choice=getNum()

EUR=convEUR(money)
match choice:
    case 1:
        convValue=convJPY(EUR)
        printConsole(round(EUR, 2), round(convValue, 2), "JPY")
    case 2:
        convValue=convUSD(EUR)
        printConsole(round(EUR, 2), round(convValue, 2), "USD")
    case 3:
        convValue=convCHF(EUR)
        printConsole(round(EUR, 2), round(convValue, 2), "CHF")
