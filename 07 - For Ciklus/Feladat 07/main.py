start: int = None
end: int = None

print("Kérem az intervallum kezdő és vég értékét!")
start=int(input())
end=int(input())

for i in range(start, end - 1, -1):
    print(i)