start: int=None
end: int=None
eredmeny: int=0

print("Kérem a kezdő és a végző értékeket!")
start=int(input())
end=int(input())

for i in range(start, end + 1, 1):
    if(i % 2 == 1 and i % 3 == 0):
        eredmeny=eredmeny+1
print(f"A páratlan számok közül hárommal osztható számok száma: {eredmeny}")