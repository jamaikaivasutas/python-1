from os import system
from netfunctions import *
from consoleio import *

number1: float = None
number2: float = None
eredmeny: float = None

system('cls')

number1=getNumber()
number2=getNumber()

eredmeny=osszead(number1, number2)
printConsole(number1, number2, "+", eredmeny)

eredmeny=kivon(number1, number2)
printConsole(number1, number2, "-", eredmeny)

eredmeny=szoroz(number1, number2)
printConsole(number1, number2, "*", eredmeny)

eredmeny=kivon(number1, number2)
printConsole(number1, number2, "-", eredmeny)