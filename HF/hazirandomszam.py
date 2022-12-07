import random
import math

n=[]
for i in range(10):
    n.append(random.randint(1,31))

h=[]
for i in range(10):
    h.append(random.randint(1,12))

l=[]
for i in range(10):
    l.append(random.randint(1900,1999))
print("Évszám="+str(l))
print()
print("Hónap="+str(h))
print()
print("Nap="+str(n))
print()
#for i in range(10):
    #print(str(l[1])+"."+str(h[1])+"."+str(n[1]))
#Nem tudtam jobb megoldást rá :(
print(str(l[0])+"."+str(h[0])+"."+str(n[0]))
print(str(l[1])+"."+str(h[1])+"."+str(n[1]))
print(str(l[2])+"."+str(h[2])+"."+str(n[2]))
print(str(l[3])+"."+str(h[3])+"."+str(n[3]))
print(str(l[4])+"."+str(h[4])+"."+str(n[4]))
print(str(l[5])+"."+str(h[5])+"."+str(n[5]))
print(str(l[6])+"."+str(h[6])+"."+str(n[6]))
print(str(l[7])+"."+str(h[7])+"."+str(n[7]))
print(str(l[8])+"."+str(h[8])+"."+str(n[8]))
print(str(l[9])+"."+str(h[9])+"."+str(n[9]))
print()
   


atlag=sum(l)/len(l)
print("Átlag="+str(atlag))
