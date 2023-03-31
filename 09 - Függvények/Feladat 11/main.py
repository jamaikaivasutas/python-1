from os import system
from consoleio import *

system('cls')

name1: str = None
name2: str = None
name3: str = None
name4: str = None
name5: str = None

work1: int = None
work2: int = None
work3: int = None
work4: int = None
work5: int = None

earning1: int = None
earning2: int = None
earning3: int = None
earning4: int = None
earning5: int = None

name1=getName()
work1=getWork()

name2=getName()
work2=getWork()

name3=getName()
work3=getWork()

name4=getName()
work4=getWork()

name5=getName()
work5=getWork()

earning1=earn(work1)
earning2=earn(work2)
earning3=earn(work3)
earning4=earn(work4)
earning5=earn(work5)

system('cls')

printConsole(name1, name2, name3, name4, name5, work1, work2, work3, work4, work5, earning1, earning2, earning3, earning4, earning5)
