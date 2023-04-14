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


def forgat(pontok, szog):
    vissza=[]
    for i, pont in enumerate(pontok):
        if i%2 == 0:
            x=pontok[i]*math.cos(math.radians(szog)) - pontok[i+1]*math



win=Tk()

win.geometry("1920x1080")

canvas=Canvas(win, width=500, height=300,bg="skyblue")
canvas.pack(fill = BOTH, expand =1)




#canvas.create_line(250,0,250,500, fill="blue", width=5)
#canvas.create_line(500,0,500,500, fill="blue", width=5)
#canvas.create_line(750,0,750,500, fill="blue", width=5)


"""#Á
canvas.create_line(0,375,125,125,250,375,175,375,150,300,100,300,75,375,0,375, fill="red", width=10)
canvas.create_line(100,250,125,200,150,250,100,250,fill="orange", width=10)
canvas.create_line(175,150,175,100,200,100,200,150,175,150,fill="yellow", width=10)

#K
canvas.create_line(250,375,250,125,333,125,333,250,416,125,500,125,417,250,500,375,416,375,360,300,333,375,250,375,fill="green", width=10)

#O
canvas.create_line(500,125,750,125,750,375,500,375,500,125,fill="blue", width=10)
canvas.create_line(550,175,700,175,700,325,550,325,550,175,fill="indigo", width=10)

#S
canvas.create_line(1000,125,750,125,750,249,936,249,936,311,750,311,750,375,1000,375,1000,210,812,210,810,160,1000,160,1000,125,fill="violet", width=10)
"""
A=[0,375,125,125,250,375,175,375,150,300,100,300,75,375,0,375,]
kisA=[100,250,125,200,150,250,100,250,]
vesszo=[175,150,175,100,200,100,200,150,175,150,]
K=[250,375,250,125,333,125,333,250,416,125,500,125,417,250,500,375,416,375,360,300,333,375,250,375,]
O=[500,125,750,125,750,375,500,375,500,125,]
kisO=[550,175,700,175,700,325,550,325,550,175,]
S=[1000,125,750,125,750,249,936,249,936,311,750,311,750,375,1000,375,1000,210,812,210,810,160,1000,160,1000,125,]

K=eltol(K,100,0)
K=nagyit(K,2)
#canvas.create_line(A,fill="red",width=10)
#canvas.create_line(kisA,fill="orange",width=10)
#canvas.create_line(vesszo,fill="yellow",width=10)
canvas.create_line(K,fill="green",width=10)
#canvas.create_line(O,fill="blue",width=10)
#canvas.create_line(kisO,fill="indigo",width=10)
#canvas.create_line(S,fill="violet",width=10)



win.mainloop()
