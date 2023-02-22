from os import system
from time import process_time_ns

number : int = None
temp : str = None
isNumber : bool = None
truncatedString : str = None
osszeg : int = 0
oszthato : int = 0

system('cls')

while(number == None):
    print("Kérek egy kétjegyű, pozitív számot!")
    temp = str(input())
    truncatedString = temp.replace(".", "").replace(" ", "").replace("-", "")
    isNumber = truncatedString.isnumeric()
    if(isNumber and (len(temp) == 2 and int(temp) >= 0)):
        number=int(temp)

for i in range(0, number + 1, 1):
    if(i % 5 == 0):
        osszeg=osszeg+i
    if(i % 11 == 0):
        oszthato=oszthato+1
if(isNumber == False):
    print("Nem számot adott meg!")                
elif(int(temp) < 0):
    print("Nem pozitív számot adott meg!")
else:
    print("Nem kétjegyű számot adott meg!")

print("Páros számok:")
for i in range(0, number + 1, 2):
    print(i)
print(f"5-tel osztható számok összege: {osszeg}")
print(f"11-el osztható számok száma: {oszthato}")
print("7-tel elosztott számok 3 maradékkal:")
for i in range(0, number + 1, 1):
    if(i% 7 == 3):
        print(i)
