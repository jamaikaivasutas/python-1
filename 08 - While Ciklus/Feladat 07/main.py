from os import system

system('cls')

number1: int = None
number2: int = 0
temp: str = None
jump: int = None
truncatedString: str = None

while(number1 == None):
    print("Kérek egy számot!")
    temp = input()
    truncatedString = temp.replace(".","").replace("-","")
    isNumber = truncatedString.isnumeric()

    if(isNumber):
        number1 = int(temp)
    else:
        print("Nem számot adott meg!")

while(number1 >= number2):
    print("Kérek egy nagyobb számot!")
    temp = input()
    truncatedString = temp.replace(".","").replace("-","")
    isNumber = truncatedString.isnumeric()

    if(isNumber):
        number2 = int(temp)
    else:
        print("Nem számot adott meg!")
    
while(jump == None):
    print("Kérem a lépésközt!")
    temp = input()
    truncatedString = temp.replace(".","").replace("-","")
    isNumber = truncatedString.isnumeric()

    if(isNumber):
        jump = int(temp)
    else:
        print("Nem számot adott meg!")

system('cls')

for i in range(number1, number2 + 1, jump):
    print(i)
