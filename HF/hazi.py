f=open("proba.txt","w")
szoveg = []
betu = "sad"
while betu != "":
    betu=input("Kérek valami szöveget: ")
    f.write(betu)
    f.write("\n")
f.close()

f = open("proba.txt","r")
a = f.read()
f.close()
print(a)

