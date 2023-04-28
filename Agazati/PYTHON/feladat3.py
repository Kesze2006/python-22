
def ido2mp():







#1

eredmenyek=[]

f=open("triatlon.txt")

for egySor in f:
    temp=egySor.replace("\n","").split(";")
    eredmenyek.append(temp)

f.close()
eredmenyek.pop(0)
#print(eredmenyek)

#2
print("2. feladat")
print("A versenyen {} versenyző indult.".format(len(eredmenyek)))
#3
print("3. feladat")

