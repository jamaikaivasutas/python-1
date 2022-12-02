import math

hossz: int=None
szel: int=None

valasztas: str=None
eredmeny: int=None

print("Kérem a téglalap hosszát (cm)!")
hossz=int(input())
print("Kérem a téglalap szélességét!")
szel=int(input())

print("Kérem válasszon a menüből!\nt - terület\nk - kerület\na - átló")
valasztas=str(input().lower().strip())

match valasztas:
    case "t":
        eredmeny=hossz*szel
        print(f"A téglalap területe: {eredmeny} cm")
    case "k":
        eredmeny=(hossz+szel)*2
        print(f"A téglalap kerülete: {eredmeny} cm")
    case "a":
        eredmeny=math.sqrt(math.pow(hossz)+math.pow(szel))
        print(f"A téglalap átlója: {eredmeny} cm")
