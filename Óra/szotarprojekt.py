import random

def szobeker():
    szo=input("Kérek egy szót: ")
    if szo=="":
        jelentes=""
    else:
        jelentes=input(szo+ " jelentése: ")
    return [szo,jelentes]

szavak=[]
def sokbeker():
    szo=szobeker()
    while szo[0]!="":
        szavak.append(szo)
        szo=szobeker()


    return(szavak)
#print(sokbeker())

def filebair(lista):
    f=open("szotar.txt","a")

    for e in lista:
        #print(e)
        f.write(" ".join(e))
        f.write("\n")

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
    #print("valasztott",valasztott)
    rossz=[]
    for i in range(3):
        temp=random.choice(kerdesek)
        #print("temp",temp)
        while not(temp not in rossz and temp != valasztott):
            temp=random.choice(kerdesek)
            
        rossz.append(temp)
        #print("rossz",rossz)    

    print("-"*40)
    print("Mit jelent: "+ valasztott[0]+"?")

    rossz.append(valasztott)
    
    #valasz bekeres
    abc="abcdefghijklmnopqrstuvz"
    random.shuffle(rossz)

    i=0
    for e in rossz:
        print(abc[i]+": "+e[1])
        i+=1
    valasz=input("Válassz: ")          

    hol=4
    while hol>=4:
        try:
            if valasz!="":
                hol=abc.index(valasz)
        except:
            valasz=input("valassz ujra : ")
        else:
            if hol>=4:
                valasz=input("valassz ujra : ")
            
    #if valasztott[0]==rossz[hol][0]:
        #print("helyes :)")
    #else:
        #print("rossz a válasz :(")

    return valasztott[0]==rossz[hol][0]

def menu():
    beker=""

        
    while beker!="0":
        print("-"*40)
        print("szótár program\n")
        print("1: Szavak bevitele")
        print("2: Feleltetes")
        print("0: Kilepes")
        beker=input("Válasz: ")

        if beker=='1':
            #adatbekeres
            szavak=sokbeker
            filebair(szavak)
            
        elif beker=="2":
            #feleltetés   
            beolvas()
            lil_A=[]
            for i in range(10):
                lil_A.append(kerdez())
            #print(lil_A)
            print("Az eredmeny: {:.0%}".format(lil_A.count(True)/len(lil_A)))   
menu()
    




    

