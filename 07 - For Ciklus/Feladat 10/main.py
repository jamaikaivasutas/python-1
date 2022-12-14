from time import process_time_ns


start: int=None
end: int=None
osszeg: int=0
szorzat:int=1

print("Kérem a kezdő és a végző értékeket!")
start=int(input())
end=int(input())

if(end > start):
    for i in range(start, end + 1):
        osszeg=osszeg+i
        szorzat=szorzat*i
else:
    for i in range(end, start + 1):
        osszeg=osszeg+i
        szorzat=szorzat*i

print(osszeg)
print(szorzat)
