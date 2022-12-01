
lista=[]
while len(lista)<10:
    for i in range(10):
        try:
            lista.append(int(input("Kérek egy számot(lista): ")))
        except:
            print("Hiba!")


    
print(lista)

for i in range(len(lista)):
    print(lista[i],end=" ")
    if i%3==2:
        print()

print()

szamBe=""
while szamBe=="":
    try:
        szamBe=int(input("Kérek egy számot: "))
    except:
        print("Nem szám!")



if szamBe in lista:
    print("Van benne")
else:
    print("Nincs benne")

def oszlopba(munkalista,db):
    for i in range(len(munkalista)):
        print(munkalista[i],end=" ")
    if i%db==db-1:
        print()
    print()



oszlopba(lista,2)
