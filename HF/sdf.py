import random
szavak=["alma","körte","barack","banón","dinnye","szőlő"]

nagylista = []
for e in szavak:
        kislista=[]
        kislista.append(e)
        kislista.append(random.randint(1,98))
        #print(kislista)
        k=[]
        k.append(kislista)
        nagylista.append(kislista)
        #print(nagylista)

    #for e in nagylista:
     #   print(e[0].ljust(10),str().rjust(10))
      #  print("kg")

print()
print("1 - enyenlő 1 kg-al")
print()
for e in nagylista:
    print(".",e[0].ljust(5),end=" ")
    print("-"*e[1],e[1])
print("."*108)
print("kg".center(105))
#print("dinnye","-"*97,"100")
