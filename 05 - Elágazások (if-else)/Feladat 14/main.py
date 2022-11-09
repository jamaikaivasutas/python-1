from os import system

x: int=None
y: int=None
z: int=None

system("cls")

print("Kérek egy számot (x)!")
x=int(input())

print("Kérek egy számot (y)!")
y=int(input())

print("Kérek egy számot (z)!")
z=int(input())

if(x%y == 0 and x%z == 0):
    print("A szám y-nal és z-vel is osztható.")
elif(x%y == 0):
    print("A szám osztható y-nal")
elif(x%z == 0):
    print("A szám osztható z-vel")
else:
    print("Egyik számmal se oszható.")