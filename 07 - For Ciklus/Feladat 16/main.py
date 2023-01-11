start: int=None
end: int=None
osszegParos: int=0
osszegParatlan: int=0
atlag: int=None

print("Kérem az intervallum kezdő és a végző értékét.")
start=int(input())
end=int(input())

for i in range(start, end + 1, 1):
    if(i % 2 == 0):
        osszegParos=osszegParos+i
    else:
        osszegParatlan=osszegParatlan+i

atlag=(osszegParatlan+osszegParos)/2

print(f"A páratlan számok összegének és a páros számok összegének az átlaga: {atlag}")