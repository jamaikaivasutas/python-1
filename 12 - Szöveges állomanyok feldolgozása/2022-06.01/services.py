from grade import Grade
from typing import *

def printToConsole(grades: List[Grade])->None:
    for grade in grades:
        print(grade)

def countGrades(grades: List[Grade])->int:
    return len(grades)

def countFailed(grades: List[Grade])->int:
    failed: int = 0
    
    for grade in grades:
        if(grade.grade == 1):
            failed += 1
    return failed

def writeExcelent(grades: List[Grade]):
    excelent: List[str] = []
    for grade in grades:
        if(grade.grade == 5):
            excelent.append(f"{grade.firstName} {grade.lastName}")
            
    return excelent

def countAverage(grades: List[Grade], year: str)->float:
    sum: int = 0
    count: int = 0
    for grade in grades:
        if(grade.year == year):
            sum += grade.grade
            count += 1

    return sum/count