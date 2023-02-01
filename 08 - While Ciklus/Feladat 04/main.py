from os import system

system('cls')

number: int = None
sum: int = 0

while(sum <= 100):
    print("Kérek egy számot!")
    number = int(input())
    sum= sum + number
    print(f"A jelenlegi összeg: {sum}")

print("Az összeg meghaladta a százat!")