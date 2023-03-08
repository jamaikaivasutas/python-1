from os import system
from consoleio import *


system ('cls')

age: int = None
name: str = None

name = getName()
age = getAge()
printName(name, age)