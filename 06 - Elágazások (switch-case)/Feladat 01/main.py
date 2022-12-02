day: int = None

print("Hanyadik napja van a hétnek?")
day = int(input().strip())

match day:
    case 1:
        print("Hétfő")
    case 2:
        print("Kedd")
    case 3: 
        print("Szerda")
    case 4:
        print("Csütörtök")
    case 5:
        print("Péntek")
    case 6:
        print("Szombat")
    case 7:
        print("Vasárnap")
    case _:
        print("Ilyen nap nincs a héten, mert egy hétben csak hét nap van.")