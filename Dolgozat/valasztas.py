#1
f = open("szavazatok.txt","r")
#2
egesz=[]
for sor in f:
    temp=sor.replace("\n","").split(" ")
    egesz.append(temp)   
f.close()
a=len(egesz)
print("A helyhatósági választáson {} képviselő jelölt indult.".format(a))

#3
print("3.feladat")
vezetek=input("Kérek egy vezetéknevet: ")
uto=input("Kérek egy utónevet: ")
szavazat=""
for e in egesz:
    if e[2] == vezetek and e[3] == uto:
        szavazat=e[1]

if szavazat == "":
    print("Ilyen nevű képviselő nem szerepel a nyílvántartásban.")
else:
    print("{} szavazatot kapott".format(szavazat))
#4
print("4. feladat")
szavazatok=0
for e in egesz:
    szavazatok += int(e[1])

a=szavazatok/(int(12345))
print("{0:.2f}%".format(a*100))
#5
print("5.feladat")
GYEP=[]
ZEP=[]
HEP=[]
TISZ=[]
fuggetlen=[]
for e in egesz:
    if e[-1] == "GYEP":
        GYEP.append(int(e[1]))
for e in egesz:
    if e[-1] == "ZEP":
        ZEP.append(int(e[1]))
for e in egesz:
    if e[-1] == "HEP":
        HEP.append(int(e[1]))
for e in egesz:
    if e[-1] == "TISZ":
        TISZ.append(int(e[1]))
    elif e[-1] == "-":
        fuggetlen.append(int(e[1]))

a=int(sum(GYEP))/(int(szavazatok))
print("GYEP= "+str(a*100)+"%")
a=int(sum(ZEP))/(int(szavazatok))
print("ZEP= "+str(a*100)+"%")
a=int(sum(HEP))/(int(szavazatok))
print("HEP= "+str(a*100)+"%")
a=int(sum(TISZ))/(int(szavazatok))
print("TISZ= "+str(a*100)+"%")
a=int(sum(fuggetlen))/(int(szavazatok))
print("Független jelöltek= "+str(a*100)+"%")
#6
print("6. feladat")














