from typing import *
import os
from grade import Grade

def readGradesFromFile(filename: str)->List[Grade]:
    grades: List[Grade] = []
    grade: Grade = None

    basepath: str = os.path.dirname(os.path.abspath(__file__))
    fileFullPath: str = os.path.join(basepath, filename)

    try:
        with open(fileFullPath, encoding="utf-8", mode="r") as file:
            for line in file:
                oneLine = line.strip()
                data = oneLine.split(" ")

                grade = Grade()
                grade.firstName = data[0]
                grade.lastName = data[1]
                grade.year = data[2]
                grade.grade = int(data[3])

                grades.append(grade)
        return grades
    except FileNotFoundError as ex:
        print(f"{FileNotFoundError} hiba lépett fel a beolvasás közben.")
        return []



