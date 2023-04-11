import random
def mock(s):
    res = ""
    i = True
    for char in s:
        if i:
            res += char.upper()
        else:
            res += char.lower()
        i = not i
    return res

hely=random.randint(1,25)
versek=["Rózsa, rózsa szép virágszál, Szálló szélben hajladozzál. Napsütésben nyiladozzál, Meglocsollak, illatozzál.","Én vagyok a török, locsolkodni jövök. Ha nem kapok piros tojást, mindent összetörök!","Láttam és találtam egy szép virágszálra, Engedelmet kérek meglocsolására.","Van nekem egy kis locsolóm, Kölni nincsen benn most elővenném, Nagy röhögés lenne."]
penz=random.randint(0,15000)
tojas=random.randint(0,hely)
pia=random.randint(0,hely)

class locsolo:
    penz,tojas,pia,vers=["",0,0,""]
    def __init__(self,penz,tojas,pia,vers):
        self.penz=penz
        self.tojas=tojas
        self.pia=pia
        self.vers=vers
    def locsolas(self):
        print("{} felest ittam.".format(self.pia))
        if pia > 5:
            print(mock(self.vers))
        else:
            print(self.vers)
            
        print("Eddig {} helyen jártam és {}-Ft kaptam + {} tojást.".format(hely,self.penz,self.tojas))    
locsolo1=locsolo(penz,tojas,pia,random.choice(versek))
locsolo1.locsolas()
penz=random.randint(0,1000)
tojas=random.randint(0,3)
pia=random.randint(0,5)
class lany:
    penz,tojas,pia=[0,"",""]
    def __init__(self,penz,tojas,pia):
        self.penz=penz
        self.tojas=tojas
        self.pia=pia
    def ajandek(self):
        tetszes=["igen","nem"]
        if random.choice(tetszes) == "nem":
            print("Nem tetszett így csak 1 tojast kapsz.")
        else:
            print("Tetszet így a jutalmad {} tojás, {}-Ft pénz és {} feles.".format(self.tojas,self.penz,self.pia))
print()            
lany1=lany(penz,tojas,pia)
lany1.ajandek()









    

