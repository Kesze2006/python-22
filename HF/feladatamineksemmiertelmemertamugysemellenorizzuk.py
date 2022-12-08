import random
import math


sz=[]
for i in  range(100):
    sz.append(random.randint(1000,9999))

l6=[]
for e in sz:
    if e%12==0:
        pass
    elif e%6==0:
        l6.append(e)
    else:
        pass

print(l6)
