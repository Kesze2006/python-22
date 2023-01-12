#1
szam = []

for i in range(7):
    szam.append(int(input("Kérek egy számot: ")))

#2
print(szam[::-1])
print()
#3
for i in range(7):
    if i%5==0:
        print()
    print(szam[i],end=" ")
print()

#4
print()
osszeg = sum(szam)
print(osszeg)

#5
szoveg = "Nulla quis mi augue. Nunc vel pretium lectus. Aenean laoreet ornare ornare. Ut vitae elit et sapien fringilla iaculis ac at felis. Aenean scelerisque, diam non pellentesque rhoncus, risus lorem porttitor leo, ac consectetur nisi massa vitae sem. Nulla tempus diam id bibendum lobortis. Vestibulum porta neque id risus cursus, eget sodales nunc fermentum. Nulla facilisi. Suspendisse egestas orci a luctus fringilla. Cras dapibus ipsum nisl, non dapibus ex fermentum vitae."
print(szoveg)

#6,7
betu=""

while betu != "fin":
    betu = input("Kérek egy betüt: ")
    if betu in szoveg:
        print((szoveg.index(betu)))
    betu = input("Kérsz újat?: ")
#8
szoveg2 = szoveg.split(".")

print(szoveg2[::-1])

#9
print(len(szoveg))
szoveg3 = szoveg.replace("a","")
print(len(szoveg3))
szoveg4 = szoveg3.replace("e","")
print(len(szoveg4))

#10
szo=[3,2,1,0,2,1,0,2,1,0,3,2]
darab=[1,3,5,7,3,5,7,3,5,7,1,3]

karakter= input("Adj meg egy karaktert: ")






