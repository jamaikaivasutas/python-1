jeloles: str = None

ellenallas1: float=None
ellenallas2: float=None

eredmemy: float=None

print("Kérem az ellenállások értékeit!")
ellenallas1=float(input())
ellenallas2=float(input())

print("Kérem a kötések jelölését!")
jeloles=str(input())

match jeloles:
    case "s" | "S":
        eredmemy=ellenallas1+ellenallas2
        print(f"Az eredmény: {eredmemy}")
    case "p" | "P":
        eredmemy=(ellenallas1+ellenallas2)/(ellenallas1*ellenallas2)
        print(f"Az edemény: {eredmemy}")

