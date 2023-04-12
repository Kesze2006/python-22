class orszag(): #regnum
    def __init__(self,orszag):
        slef.orszag=orszag


class torzs(orszag): #divisio
    def __init__(self,orszag,torzs):
        super().__init__(orszag)
        self.torzs=torzs

class altorzs(torzs):
    def __init__(self,o,t,at):
        super().__init__(o,t)
        self.altorzs=a

class foosztaly(altorzs):
    def __init__(self,o,t,at,fo):
        super().__init__(o,t,at)
        self.fofosztaly=fo

class osztaly(foosztaly): #classis
    def __init__(self,o,t,at,fo,osz):
        super().__init__(o,t,at,fo)
        self.osztaly=osz

class alosztaly(osztaly):
    def __init__(self,o,t,at,fo,osz,aosz):
        super().__init__(o,t,at,fo,osz)
        self.alosztaly=aosz

class alosztalyag(alosztaly):
    def __init__(self,o,t,at,fo,osz,aosz,aosza):
        super().__init__(o,t,at,fo,osz,aosz)
        self.alosztalyag=aosza

class oregrend(alosztalyag):
    def __init__(self,o,t,at,fo,osz,aosz,aosza,og):
        super().__init__(o,t,at,fo,osz,aosz,aosza)
        self.oregrend=og

class rend(oregrend): #ordo
    def __init__(self,o,t,at,fo,osz,aosz,aosza,og,r):
        super().__init__(o,t,at,fo,osz,aosz,aosza,og)
        self.rend=r

class alrend(rend):
    def __init__(self,o,t,at,fo,osz,aosz,aosza,og,r,ar):
        super().__init__(o,t,at,fo,osz,aosz,aosza,og,r,)
        self.alrend=ar

class csalad(alrend): #familia
    def __init__(self,o,t,at,fo,osz,aosz,aosza,og,r,ar,cs):
        super().__init__(o,t,at,fo,osz,aosz,aosza,og,r,ar)
        self.csalad=cs

class nemzetseg(csalad):        
    def __init__(self,o,t,at,fo,osz,aosz,aosza,og,r,ar,cs,n):
        super().__init__(o,t,at,fo,osz,aosz,aosza,og,r,ar,cs)
        self.nemzetseg=n

class nem(nemzetseg): #genus
    def __init__(self,o,t,at,fo,osz,aosz,aosza,og,r,ar,cs,n,nem):
        super().__init__(o,t,at,fo,osz,aosz,aosza,og,r,ar,cs,n)
        self.nem=nem

class faj(nem): #species
    def __init__(self,o,t,at,fo,osz,aosz,aosza,og,r,ar,cs,n,nem,f):
        super().__init__(o,t,at,fo,osz,aosz,aosza,og,r,ar,cs,n,nem)
        self.faj=f
    
    




