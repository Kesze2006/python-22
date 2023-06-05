def haromszog():
    szamok=[]
    for e in range(3):
        szam=""
        while szam == "":
            try:
                szam=int(input("Kérek egy számot: "))
                szamok.append(szam)
            except:
                print("Ez nem szám!")
haromszog()


