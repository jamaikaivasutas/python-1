from typing import *
from student import Student
from studentIO import *
from services import *

students: List[Student] = importStudents()

#1 - Írjuk ki minden diák adatát a képernyőre!
print("Az osztaly tanuloi:")
for student in students:
    print(student)

#2 - Hány diák jár az osztályba?
countOfClass: int = len(students)
print(f"\n\nAz osztalynak {countOfClass} tanuloja van.")

#3 - Mennyi az osztály átlaga?
classAverage: float = calculateAverage(students)
print(f"\n\nAz osztaly atlaga: {classAverage:1.2f}")

#4 - Keressük a legtöbb pontot elért érettségizőt és írjuk ki az adatait a képernyőre.
bestStudent: Student = getBestStudent(students)
print(f"\n\nA legjobb tanulo: {bestStudent}")

#5 - atlagfelett.txt allományba keressük ki azon tanulókat kiknek pontjai meghaladják az átlagot!
aboveAverage: List[Student] = studentAboveAverage(students, classAverage)
writeStudentInFile(aboveAverage, "atlagfelett.txt")

#6 - Van e kitünő tanulónk?
if(isAnyExcellentStudent(students)):
    print("\nVan kitünő tanuló")
else:
    print("\nNincs kitünő tanuló.")

"""
7 - Hány elégtelen, elégséges, jó, jeles és kitünő tanuló van az osztályban?
    Értékhatárok:
 - elégtelen, ha: 0.00 - 1.99
 - elégséges, ha: 2.00 - 2.99
 - jó, ha: 3.00 - 3.99
 - jeles, ha: 4.00 - 4.99
 - kitünő, ha: 5.00
 """