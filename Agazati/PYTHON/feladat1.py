print("1. feladat")
szoveg = input("Kérek egy szöveget: ")
szam=""
while szam == "":
    try:
        szam = int(input("Kérek egy egész számot:"))
    except:
        print("Ez nem egész szám!")
if len(szoveg) > szam:
    print(szoveg[szam]*szam)
else:
    print("Sajnos nincs ilyen betű!")
