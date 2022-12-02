choice: int = None

print("Kérem válasszon egy üdítőt!")
print("1 - Coca Cola\n2 - Pepsi\n3 - Fanta\n4 - Sprite")
choice = int(input().strip())

match choice:
    case 1:
        print("A Coca Cola ki lett adva.")
    case 2:
        print("A Pepsi ki lett adva.")
    case 3:
        print("A Fanta ki lett adva.")
    case 4:
        print("A Sprite ki lett adva.")
    case _:
        print("Ilyen üdítő nincsen.")