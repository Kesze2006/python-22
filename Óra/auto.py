import random
class auto:
    szin=""
    ajtokszama=0
    marka=""
    tipus=""
    def __init__(self,szin,ajtokszama,marka,tipus):
        self.szin=szin
        self.ajtokszama=ajtokszama
        self.marka=marka
        self.tipus=tipus
    def inditas(self):
        print("Brr-rr!")
    def duda(self):
        print("Tü-Tü!")
    def index(self):
        print("Kat-Kat!")

    def __str__(self):
        return self.marka
    

if __name__ == '__main__':
    q=auto("piros",5,"Nissan","GTR")
    print(q)
    q.inditas()
    q.duda()
    q.index()
    print()

class bmw(auto):
    def __init__(self,szin,ajtokszama,marka,tipus):
        super().__init__(szin,ajtokszama,marka,tipus)

    def inditas(self):
        print("Brum!!")
    def index(self):
        print("*Tücsökciripelés*")

    def __str__(self):
        return self.marka


if __name__ == '__main__':
    bmw=bmw("fekete",5,"BMW","e34")
    print(bmw)
    bmw.inditas()
    bmw.index()
    bmw.duda()
    print()


class merci(auto):
    def __init__(self,szin,ajtokszama,marka,tipus):
        super().__init__(szin,ajtokszama,marka,tipus)

    def duda(self):
        print("Du-Du!")
        
    def __str__(self):
        return self.marka

if __name__ == '__main__':
    merci=merci("lila",3,"Mercédesz","B-osztály")
    print(merci)
    merci.inditas()
    merci.index()
    merci.duda()
    print()

class audi(auto):
    def __init__(self,szin,ajtokszama,marka,tipus):
        super().__init__(szin,ajtokszama,marka,tipus)
    a=random.randint(1,2)
    def checkengine(self):
        pass
    if a == 1:
        engine=True
    else:
        engine=False
        
    if engine == True:
        def checkengine(self):
            print("Ég a check engine!!")


if __name__ == '__main__':
    audi=audi("sárga",5,"Audi","RS6")
    print(audi)
    audi.inditas()
    audi.index()
    audi.duda()
    audi.checkengine()
    print()


    
