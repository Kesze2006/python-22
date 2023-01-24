import random

def szobeker():
    szo = input("Kérek egy szót: ")
    if szo == "":
        jelentes=""
    else:
        jelentes=input("Mit jelenet az hogy "+szo+"?")
    return [szo,jelentes]


szavak=[]
def sokbeker():
    szo=szobeker()
    while szo[0] != "":
        szavak.append(szo)
        szo=szobeker()
    return(szavak)


def filebair(lista):
    f=open("szotar.txt","a")
    for e in lista:
        f.write(" ".join(e))
        f.write("\n")
        #print(e)
        
    f.close()

kerdesek=[]
def beolvas():
    f=open("szotar.txt","r")
    for sor in f:
        kerdesek.append(sor.replace("\n","").split(" "))
    
    f.close()
def kerdez():
    #random.seed(2)
    valasztott=random.choice(kerdesek)
    #print("valasztott:",valasztott)
    rossz=[]
    for i in range(3):
        temp=random.choice(kerdesek)
        #print("temp",temp)
        while not(temp not in rossz and temp != valasztott):
            temp=random.choice(kerdesek)
            
        rossz.append(temp)
        #print("rossz", rossz)   
    print("-"*40)
    print("Mit jelent: " + valasztott[0] + "?")
    
    rossz.append(valasztott)
    #print(rossz)


    abc="abcdefghijklmnopqrstuvxyz"
    random.shuffle(rossz)

    i=0
    for e in rossz:
        print(abc[i]+": "+e[1])
        i+=1

    valasz=input("Válassz: ")
    hol=abc.index(valasz)
    print(hol)
    while hol >= 4:
        try:
            valasz=input("Válassz újra: ")
            hol=abc.index(valasz)
        except:
            print("Hiba")
        
beolvas()
kerdez()
#szavak=sokbeker()
#filebair(szavak)

 
