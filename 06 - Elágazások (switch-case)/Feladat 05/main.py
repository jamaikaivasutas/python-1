jeloles: str = None

ellenallas1: float=None
ellenallas2: float=None

eredmemy: float=None

print("Kérem az ellenállások értékeit!")
ellenallas1=float(input().strip())
ellenallas2=float(input().strip())

print("Kérem a kötések jelölését!")
jeloles=str(input().lower().strip())

match jeloles:
    case "s":
        eredmemy=ellenallas1+ellenallas2
        print(f"Az eredmény: {eredmemy}")
    case "p":
        eredmemy=(ellenallas1+ellenallas2)/(ellenallas1*ellenallas2)
        print(f"Az edemény: {eredmemy}")

