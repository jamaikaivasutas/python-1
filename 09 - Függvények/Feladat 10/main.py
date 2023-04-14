from os import system
from consoleio import *

firstNum: int = None
secondNum: int = None
randomNum: int = None
trial: int = None

system('cls')

firstNum=genRnd(0,9)
secondNum=genRnd(40,50)

randomNum=genRnd(firstNum, secondNum)

trial=guess(randomNum)
print(trial)