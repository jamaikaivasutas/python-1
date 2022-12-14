start: int=None
end: int=None
osszeg: int=0
szorzat:int=1

print("Kérem a kezdő és a végző értékeket!")
start=int(input())
end=int(input())

if(start % 2 == 0):
    for i in range(start, end + 1, 2):
        osszeg=osszeg+i
    for i in range(start + 1, end + 1, 2):
        szorzat=szorzat*i
else:
    for i in range(start + 1, end + 1, 2):
        osszeg=osszeg+i
    for i in range(start, end + 1, 2):
        szorzat=szorzat*i
print(osszeg)
print(szorzat)