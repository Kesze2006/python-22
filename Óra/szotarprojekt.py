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
    print(kerdesek)


kerdez()
beolvas() 
#szavak=sokbeker()
#filebair(szavak)
