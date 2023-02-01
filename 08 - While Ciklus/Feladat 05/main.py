from os import system

system('cls')

border: int = 0
number: int = None
sum: int = 0

while(border <= 100):
    print("Kérem a határértéket!")
    border = int(input())
    if(border <= 100):
        print("Nagyobb számot adjon meg mint száz!")

while(sum <= border):
    print("Kérek egy számot!")
    number = int(input())
    sum = sum + number
    print(f"A jelenlegi összeg: {sum}")

print("Az összeg meghaladta a határértéket!")