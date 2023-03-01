#1 feladat
f = open("jarmu.txt","r")
#2 feladat
jarmu=[]
for sor in f:
    temp=sor.replace("\n","").split(",")
    jarmu.append(temp)

print(jarmu)






#3 feladat


f.close()
