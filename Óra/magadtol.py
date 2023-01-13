import random
import math
def szam():
        
            
            l=(random.randint(2003,2008))

            h=(random.randint(1,12))

            if h == 1 or h == 3 or h == 5 or h == 7 or h == 9 or h == 11:
                n=(random.randint(1,31))
            elif h == 2:
                n=(random.randint(1,28))
            else:
                n=(random.randint(1,30))
            if h < 10:
                h = "0" + str(h)
            if n < 10:
                n = "0" + str(n)
                
            return str(l)+"."+str(h)+"."+str(n)+"."+"\n"
def iras():
    f=open("fel.txt","w")
    for i in  range(10):
        f.write(szam())
    f.close()
    f=open("fel.txt","r")
    c=f.read()
    print(c)
    f.close()
iras()
