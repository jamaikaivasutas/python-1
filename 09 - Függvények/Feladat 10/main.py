from os import system
from consoleio import *

number1: int = None
number2: int = None
number3: int = None
trial: int = None

system('cls')

number1=genRnd(0,9)
number2=genRnd(40,50)

number3=genRnd(number1, number2)

trial=guess(number1, number2, number3)
print(trial)