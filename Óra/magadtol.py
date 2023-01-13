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
    l.append(random.randint(2003,2008))
print("Évszám="+str(l))
print()
print("Hónap="+str(h))
print()
print("Nap="+str(n))
print()
o=[]
k=[]
f=[]
for e in l:
    o.append(str(e))
for r in h:
    k.append(str(r))
for t in n:
    f.append(str(t))

print(str(e)+str(r)+str(t))
print(o+k+f)
