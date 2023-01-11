start: int=None
end: int=None
eredmeny: int=0

print("Kérem a kezdő és a végző értékeket!")
start=int(input())
end=int(input())

if(start % 3 == 0):
    for i in range(start, end + 1, 3):
        eredmeny=eredmeny+1
elif(start % 3 == 1):
    for i in range(start + 2, end + 1, 3):
        eredmeny=eredmeny+1
else:
    for i in range(start + 1, end + 1, 3):
        eredmeny=eredmeny+1
print(f"Hárommal osztható számok száma: {eredmeny}")