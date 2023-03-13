def oszlopvissza(hanyadik):
    oszlop=[]
    for e in tabla:
        oszlop.append(e[hanyadik-1])
    return oszlop
    
def alma(hanyasaval):
    oszlop=[e[hanyasaval-1::hanyasaval] for e in tabla]
    return oszlop




gyumolcsok=["alma","körte","szőlő","barac","dragonfruit","licsi",]

print("Ennyi gyümölcs van: " + str(len(gyumolcsok)))

#gyumolcsok[3]="barack"

print(gyumolcsok.index("barac"))
index=gyumolcsok.index("barac")
gyumolcsok[index]+="k"

#print(gyumolcsok)
print("Rövid gyümölcsök")

rovid=[]
for i in range(len(gyumolcsok)):
    if len(gyumolcsok[i]) < 5:
        rovid.append(gyumolcsok[i])
    
print(rovid)

rovid=[]
for e in gyumolcsok:
    if len(e) < 5:
        rovid.append(e)
print(rovid)

rovid=[e for e in gyumolcsok if len(e) < 5]
print(rovid)

rovid=[]
i=0
while i<len(gyumolcsok):
    if len(gyumolcsok[i]) < 5:
        rovid.append(gyumolcsok[i])
    i+=1
print(rovid)

i=0
rovid=[]
while True:
    print(i)
    if len(gyumolcsok[i]) < 5:
        rovid.append(gyumolcsok[i])
        
    
    i+=1
    if len(gyumolcsok)==i:
        break

print(gyumolcsok[:2])

print(gyumolcsok[-2:])
print(gyumolcsok[len(gyumolcsok)-2:])

print(gyumolcsok[1:-1])

paratlna=gyumolcsok[1::2]
print(paratlna)

paros=gyumolcsok[::2]
print(paros)

print(gyumolcsok[::-1])

masolat=gyumolcsok
masolat.reverse()
print(masolat)

tabla=[]
for i in range(20):
    sor=[]
    for k in range(10):
        sor.append((i+1)*(k+1))
    tabla.append(sor)
print(tabla)

oszlop=[]
for e in tabla:
    #print(e)
    oszlop.append(e[0])
print(oszlop)    
print(oszlopvissza(5))
print(oszlopvissza(10))
print()
oszlop=[e[:3] for e in tabla]
oszlop=[e[4:7] for e in tabla]
oszlop=[e[3::4] for e in tabla]
print(oszlop)
print()
#print(alma (int(input("Kérek egy számot: "))))ű

oszlop=[[e[2],e[6],e[0]] for e in tabla]
print(oszlop)








