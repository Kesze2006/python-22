class ember:
    szuletes=0
    magassag=0
    suly=0
    def __init__(self,szuletes,magassag,suly):
        self.szuletes=szuletes
        self.magassag=magassag
        self.suly=suly


    def eletkor(self):
        self.szuletes=2023-self.szuletes
        print(self.szuletes)

    def tti(self):
        vissza=self.suly/(self.magassag*self.magassag)
        print(vissza)
ember1=ember(2012,172,58)
ember1.eletkor()
ember1.tti()
print()

ember2=ember(2020,54,34)
ember2.eletkor()
ember2.tti()
print()

ember3=ember(2004,195,85)
ember3.eletkor()
ember3.tti()
print()



class diak(ember):
    osztaly=""
    
    def __init__(self,szuletes,magassag,suly,osztaly):
        self.osztaly=osztaly
        super().__init__(szuletes,magassag,suly)

    def iskola(self):
        if self.szuletes < 6:
            print("Nem jár még iskolába")
        elif self.szuletes == 6:
            print("Ő az 1.{} osztályba jár".format(self.osztaly))


diak1=diak(2017,78,52,"A")
diak1.iskola()

diak2=diak(2000,158,69,"A")
diak2.iskola()




            
