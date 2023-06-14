from typing import *
from gradeIO import *
from grade import Grade
from services import *

grades: List[Grade] = []

grades = readGradesFromFile("jegyek.txt")
printToConsole(grades)

count = countGrades(grades)
print(f"{count} diák írt dolgozatot.")

failed = countFailed(grades)
print(f"{failed} diáknak nem sikerült az alapvizsgája.")

excelent = writeExcelent(grades)
print(excelent)

average = countAverage(grades, "10.a")
print(f"10.a osztály átlageredménye: {average:1.2f}")