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

if __name__ == '__main__':
    q=auto("piros",5,"BMW","e34")
    q.inditas()
    q.duda()
    q.index()


class bmw(auto):
    def __init__(self)
    super().inditas
