start: int=None
end: int=None
osszegOt: int=0
osszegHet: int=0

print("Kérem a kezdő és a végző értékeket!")
start=int(input())
end=int(input())

for i in range(start, end + 1, 1):
    if(i % 5 == 0):
        osszegOt=osszegOt+i
    if(i % 7 == 0):
        osszegHet=osszegHet+i

if(osszegHet>osszegOt):
    print(f"A héttel osztható számok összege nagyobb: {osszegHet}")
else:
    print(f"Az öttel osztható számok összege nagyobb: {osszegOt}")
