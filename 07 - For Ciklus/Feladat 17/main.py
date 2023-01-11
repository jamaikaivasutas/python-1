start: int=None
end: int=None
atlag: int=None
osszeg: int=0

print("Kérem az intervallum kezdő és a végző értékét.")
start=int(input())
end=int(input())

for i in range(start, end + 1, 1):
    osszeg=osszeg+i

atlag=osszeg/end

print(f"Az intervallum átlaga: {atlag}")
