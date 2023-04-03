
f=open("felfedezesek.csv")
elemek=[]
for e in f:
    elemek.append(e.replace("\n","").split(";"))
f.close()

elemek.pop(0)

print(elemek)
print("3. feladat: Elemek száma: "+str(len(elemek)))
okor=[ e for e in elemek if e[0]=="Ókor"]
print("4. feladat: Felfedezések száma az ókórban: "+str(len(okor)))
while True:
    vegyjel=input("5. feladat: Kérek egy vegyjelet: ").lower()
    if len(vegyjel) < 3 and len(vegyjel) > 0:
        jo=True
        for i in range(len(vegyjel)):
            if not(vegyjel[i] >= "a" and vegyjel[1] <= "z"):
                jo=False
        if jo:
            break
            
print(vegyjel)

keresett=[e for e in elemek if e[2].lower()==vegyjel ]
if keresett == []:
    print("Nincs ilyen")
else:
    print()
#print(keresett)
