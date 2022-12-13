import random
import math

l=[]
for i in range(10):
    szam=random.random()
    l.append(math.floor(szam*90)+10)
#print(l)

l=[]
for i in range(10):
    l.append(random.randint(10,99))


#print(l)
l=[]

for i in  range(100):
    l.append(random.randint(-1000,1000)*3)

print(l)

print()
print(sum(l))
l5=[]
for e in l:
    if e%5==0:
        l5.append(e)

print(l5)

l5=[e//15 for e in l if e%5==0]
print(l5)


print(random.randrange(167,1667,2)*6)

print((random.randint(83,832)*2+1)*6)
print()
print()





szavak=["alma","körte","barack","banón","dinnye","szőlő"]

#random.seed(1)
print(szavak[random.randint(0,len(szavak)-1)])


print(random.choice(szavak))


#[["alma",14]["körte",18]]
nagylista = []
for e in szavak:
        kislista=[]
        kislista.append(e)
        kislista.append(random.randint(12,312))
        #print(kislista)
        nagylista.append(kislista)
        print(nagylista)

for e in nagylista:
    print(e[0].ljust(10),str(e[1]).rjust(10),"kg")

