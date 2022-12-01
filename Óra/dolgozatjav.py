#1
szamok=[]
for i in range(10):
    szamok.append(int(input((str(i+1)+". szám: "))))

#2
for i in szamok:
    print(str(i),end="")
print()

#3
for i in range(10):
    print(str(szamok[i])+"\t",end="")
    if i%3==2:
        print()

#4

atlag=sum(szamok)/len(szamok)
print()
print(atlag)



osszeg=0

for i in szamok:
    osszeg+=i
atlag=osszeg/len(szamok)
print()
print(atlag)

#5
szoveg ="Integer eget pharetra magna. Nulla ex urna, congue ac tincidunt ut, interdum et metus. Phasellus nunc nunc, consectetur eu odio vitae, ullamcorper sagittis nisi. Ut quam tortor, tempus sit amet diam nec, auctor iaculis leo. Donec ut libero velit. Maecenas nisi magna, congue ut tortor quis, maximus maximus arcu. Mauris et commodo nibh. Fusce id est vehicula, consectetur mi et, molestie sapien."

betu="asda"
while betu!="":
    betu=input("Kérek egy betüt: " )
    szoveg=szoveg.replace(betu,betu.upper())
    print(szoveg)

#7
lista=szoveg.split(" ")
lista.reverse()
szoveg2=" ".join(lista)
print(szoveg2)




