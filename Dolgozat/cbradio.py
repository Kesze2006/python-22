orasok=[]
percsok=[]
adasdbsok=[]
nevsok=[]
cb=[]
f=open("cb.txt","r")
for e in f:
    cb.append(e.replace("\n","").split(";"))
f.close()
cb.pop(0)
for e in cb:
    orasok.append(e[0])
    percsok.append(e[1])
    adasdbsok.append(e[2])
    nevsok.append(e[3])
db=len(cb)

class cbradio:
    def __init__(self,orasok,percsok,adasdbsok,nevsok):
        self.ora=orasok
        self.perc=percsok
        self.adasdb=adasdbsok
        self.nev=nevsok
    def AtszamoloPercre(self):
        return int(self.ora)*60+int(self.perc)



        
#3
print("3. feladat: Bejegyzések száma: {} db".format(db))       
#4
for e in adasdbsok:
    if e == "4":
        print("4. feladat: Volt négy adást indító sofőr.")
        break
#5  
nevKer=input("Kérek egy nevet: ")
hivasa=[]
for e in cb:
    if e[3] == nevKer:
        hivasa.append(int(e[2]))
hanyszor=sum(hivasa)
if nevKer in nevsok:
    print("{} {}x használta a CB-rádiót.".format(nevKer,hanyszor))
else:
    print("Nincs ilyen nevű sofőr!")
#6
a=cbradio(orasok,percsok,adasdbsok,nevsok)
a.AtszamoloPercre
#7




#8
becenevek=[]
for e in nevsok:
    if e not in becenevek:
        becenevek.append(e)
    else:
        pass
print("8. feladat: Sofőrök száma: {} fő".format(len(becenevek)))

#9
nevekvalami=[]
for e in cb:
    if e[3] not in nevekvalami:
        nevekvalami.append(e[3])
hivas=[]
for e in cb:
    if e[3] == temp:
            hivas.append(e[2])
print(hivas)










