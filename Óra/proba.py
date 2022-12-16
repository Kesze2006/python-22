import random
import math

minimumErtek = int(input("Add meg, hogy hol kezdődjön: "))
maximumErtek = int(input("Add meg, hogy hol végződjön: "))
darab = int(input("Mennyi darab szám legyen: "))

lista=[]

for i in range(darab):
    lista.append((random.randint(minimumErtek,maximumErtek)))

print(lista)

legnagyobb=max(lista)
egyseg=80/legnagyobb

for e in lista:
    print("*"*math.floor(e*egyseg))


szam=""

while len(szam) != 3 :
    szam= input("Kérek egy 3 jegyű számot: ")




szam=int(szam)

if szam%12==0:
    print("Oszt ható")
else:
    print("Nem osztható")


print(szam)



szoveg = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis quis ipsum et nisi porta convallis. Sed non bibendum felis. Maecenas porttitor ligula ut hendrerit placerat. Fusce cursus tincidunt lectus. Praesent consequat scelerisque elit, vestibulum placerat justo aliquam ut. Cras lobortis feugiat sagittis. Fusce eleifend interdum lorem ac eleifend. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Vivamus luctus velit ac varius gravida. Nulla sit amet vulputate nibh. Cras sed tellus urna. Mauris pulvinar sodales nunc, nec scelerisque risus suscipit quis. Ut ultricies consequat quam, ac condimentum lectus pellentesque quis. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Proin consequat, erat nec gravida ultricies, purus eros pulvinar erat, ut imperdiet enim risus eget purus. Donec magna magna, facilisis non faucibus vel, rhoncus eu elit."


print(len(szoveg.split(" ")))


betu="i"
szoveg2 = szoveg.replace(betu,betu.upper())


print(szoveg2)








