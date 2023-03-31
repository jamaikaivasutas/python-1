from os import system
from consoleio import *

system('cls')

parameter: str = None
temperature: float=None

parameter=getParam()
temperature=getTemp()

eredmeny=atalakit(temperature, parameter)
printConsole(eredmeny, parameter)