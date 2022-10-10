beSzam=0

while (beSzam) < 2 or (beSzam) > 5 :
    beSzam = int(input("Adj meg egy számot 2 és 5 között: "))

autok = []
for i in range(0,beSzam):
    autok.append(input("Kérem a(z) "+str(i+1)+". autómárkát: "))

print(autok)

szo="almafa"

mgh= ["ö","ü","ó","e","u","o","ő","ú","a","é","á","ű","í"]
if szo[0] in mgh:
    print("az")
    
