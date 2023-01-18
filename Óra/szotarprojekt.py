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
print(sokbeker())

def filebair(lista):
    f=open("szotar.txt","a")


    f.close()
