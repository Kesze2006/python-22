#Számbekérő modul
#Többféle paraméterekkel
#"§"".''.'( łÄđzÄrÍ&zÄ ßłođ


def szamBe(szoveg,tort=False,minimum=False,maximum=False):
    #print(szoveg)
    #print(tort) 
    #rint(minimum)
    hiba = True
    while hiba: 
        try:
            if tort:
                szam = float(input(szoveg))
            else:
                szam = int(input(szoveg))
        except:
            print("Hiba!!")
        else:
            hiba = False


szamBe("Aggyá meg számót:  ",tort = True,minimum= 10)
