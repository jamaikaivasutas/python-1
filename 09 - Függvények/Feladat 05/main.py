from os import system
from consoleio import *
from stringfunctions import *

str1: str = None
str2: str = None
char: int = None

str1=getText()
str2=getText()

char=sameChar(str1, str2)

print(char)

