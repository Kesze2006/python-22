f=open("nevek.txt","r")
nev=f.read().split("\n")
f.close()
class Nev:
    def __init__(self,nev,szul):
        self.nev=nev
        self.szul=szul
    def hanyEves(self,ev):
        return ev-self.szul






































