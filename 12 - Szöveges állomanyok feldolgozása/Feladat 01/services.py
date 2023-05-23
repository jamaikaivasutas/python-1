from typing import *
from student import Student

def calculateAverage(students: List[Student]) -> float:
    sum: float = 0

    for student in students:
        sum += student.average

    return sum / len(students)

def getBestStudent(students: List[Student]) -> Student:
    bestStudent: Student = students[0] #referencia ertek

    for index in range(1, len(students), 1):
        if(students[index].average > bestStudent.average):
            bestStudent = students[index]

    return bestStudent

def studentAboveAverage(students: List[Student], classAverage: float)->List[Student]:
    aboveAverage: List[Student] = []

    for student in students:
        if(student.average >= classAverage):
            aboveAverage.append(student)
    
    return aboveAverage