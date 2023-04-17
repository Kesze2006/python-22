import math

from tkinter import *

def eltol(pontok,x,y):
    vissza=[]
    for i, pont in enumerate(pontok):
        if i%2==1:
            vissza.append(pont+y)
        else:
            vissza.append(pont+x)
    return vissza

def nagyit(pontok,meret=1):
    vissza=[]
    for pont in pontok:
        vissza.append(pont*meret)
    return vissza


def forgat(pontok,szog):
    vissza=[]
    for i, pont in enumerate(pontok):
        if i%2 == 0:
            
            
            x=pontok[i]*math.cos(math.radians(szog))-pontok[i+1]*math.sin(math.radians(szog))
            
            y=pontok[i]*math.sin(math.radians(szog))+pontok[i+1]*math.cos(math.radians(szog))
            
            vissza.append(x)
            vissza.append(y)
        return vissza        



win=Tk()

win.geometry("1920x1080")

canvas=Canvas(win, width=500, height=300,bg="skyblue")
canvas.pack(fill = BOTH, expand =1)




AKOS=[[0,375,125,125,250,375,175,375,150,300,100,300,75,375,0,375,],
      [100,250,125,200,150,250,100,250,],
      [175,150,175,100,200,100,200,150,175,150,],
      [250,375,250,125,333,125,333,250,416,125,500,125,417,250,500,375,416,375,360,300,333,375,250,375,],
      [500,125,750,125,750,375,500,375,500,125,],
      [550,175,700,175,700,325,550,325,550,175,],
      [1000,125,750,125,750,249,936,249,936,311,750,311,750,375,1000,375,1000,210,812,210,810,160,1000,160,1000,125,]]

kozep=[0,0]
db=0
for betu in AKOS:
    xK=betu[::2]
    yK=betu[1::2]
    kozep[0]+=sum(xK)
    kozep[1]+=sum(yK)
    db+=len(xK)
    
kozep[0]/=db
kozep[1]/=db




for betu in AKOS:
    betu=eltol(betu,kozep[0],kozep[1])
    betu=forgat(betu,10)
    canvas.create_line(betu,fill="black",width=10)








win.mainloop()
