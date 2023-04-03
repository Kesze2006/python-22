import random
#dice.py
kezdes=""
while kezdes == "":
    kezdes = input("Készen álsz a dobásra? (I/N) : ")
    if kezdes == "I":
        break
    elif kezdes == "N":
        break
    else:
        kezdes=""
           

print()
if kezdes == "N":
    print(":,(")
while kezdes == "I":
    szamok = [1,2,3,4,5,6]
    sorsolt = random.choice(szamok)
    if sorsolt == 1:
        print("[-----]")
        print("[     ]")
        print("[  o  ]")
        print("[     ]")
        print("[-----]")
        print()
        print("A sorsolt szám a(z) {} !".format(sorsolt))
    if sorsolt == 2:
        print("[-----]")
        print("[ o   ]")
        print("[     ]")
        print("[   o ]")
        print("[-----]")
        print()
        print("A sorsolt szám a(z) {} !".format(sorsolt))
    if sorsolt == 3:
        print("[-----]")
        print("[     ]")
        print("[o o o]")
        print("[     ]")
        print("[-----]")
        print()
        print("A sorsolt szám a(z) {} !".format(sorsolt))
    if sorsolt == 4:
        print("[-----]")
        print("[o   o]")
        print("[     ]")
        print("[o   o]")
        print("[-----]")
        print()
        print("A sorsolt szám a(z) {} !".format(sorsolt))
    if sorsolt == 5:
        print("[-----]")
        print("[o   o]")
        print("[  o  ]")
        print("[o   o]")
        print("[-----]")
        print()
        print("A sorsolt szám a(z) {} !".format(sorsolt))
    if sorsolt == 6:
        print("[-----]")
        print("[o   o]")
        print("[o   o]")
        print("[o   o]")
        print("[-----]")
        print()
        print("A sorsolt szám a(z) {} !".format(sorsolt))
    ujra=input("Szeretnél újjat sorsolni? (I/N) : ")
    if ujra == "I":
        kezdes == "i"
    else:
        print("Csá")
        break

