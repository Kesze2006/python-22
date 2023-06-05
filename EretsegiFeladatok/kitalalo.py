import modul
import random

f=open("szavak.txt")
lista=[]
for e in f:
    lista=(e.strip().replace('"',"").split(", "))
    
f.close()

szavak=[]
for e in lista:
    szavak.append(modul.szo(e))

rejtett=random.choice(szavak)
print(rejtett.szo)
tippek=[]
while True:
    tipp=input("Kérem a tippet (6 betű): ")
    tippek.append(tipp)
    if tipp == "stop":
        break

    vissza=rejtett.minta(tipp)
    
    print("Az eredmény: {}".format(vissza))
    if vissza==tipp:
        break

if tippek[-1] == "stop":
    pass
else:
