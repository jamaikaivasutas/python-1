start: int = None
end: int = None

print("Kérem az intervallum kezdő és vég értékét!")
start=int(input())
end=int(input())

if(start % 2 == 1):
    start = start - 1

for i in range(start, end - 1, -2):
    print(i)