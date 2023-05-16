class tanc:
    def __init__(self,tanc,lany,fiu):
        self.tanc=tanc
        self.lany=lany
        self.fiu=fiu
    def __str__(self):
        return "Tánc: {}, lány: {}, fiu: {}".format(self.tanc,self.lany,self.fiu)
    def isVilma(self):
        return self.lany=="Vilma"






    

f=open("tancrend.txt")

sorok=[]
#2. megoldás
tancok2=[]
temp=[]

for e in f:
    sorok.append(e.strip())
    #2. megoldás
    if len(temp) < 3:
        temp.append(e.strip())
    else:
        tancok2.append(tanc(temp[0],temp[1],temp[2]))
        temp=[]
f.close()



#1. megoldás
tancok=[]
for i in range(len(sorok)//3):
    tancnev=sorok[i*3]
    lany=[i*3+1]
    fiu=sorok[i*3+2]
    tancok.append(tanc(tancnev,lany,fiu))

#print(tancok)
#print(tancok2[2])

print("2. feladat")
print("Első tánc: {}, utolsó tánc: {}".format(tancok[0].tanc,tancok[-1].tanc))

db=0
for egyTanc in tancok:
    if egyTanc.tanc == "samba":
        db+=1
    else:
        pass
print("Ennyi szamba volt: {}".format(db))

print("Vilam ezekben szerepelt:")

for egyTanc in tancok:
    if egyTanc.isVilma():
        print(egyTanc.tanc)





