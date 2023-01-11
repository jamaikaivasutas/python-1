from time import process_time_ns


start: int=None
end: int=None
osszegParatlan: int=0
osszegParos: int=0

print("Kérem a kezdő és a végző értékeket!")
start=int(input())
end=int(input())

for i in range(start, end +1, 1):
    if(i % 2 == 0):
        osszegParos=osszegParos+i
    else:
        osszegParatlan=osszegParatlan+i

if(osszegParatlan>osszegParos):
    print(f"A páratan számok összege nagyobb: {osszegParatlan}")
else:
    print(f"A páros számok összege nagyobb: {osszegParos}")