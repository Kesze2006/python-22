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






win=Tk()

# Set the size of the tkinter window
win.geometry("700x500")

# Create a canvas widget
canvas=Canvas(win, width=500, height=300, bg="skyblue")
canvas.pack(fill = BOTH, expand = 1)


M = [100,100,300,100,300,300,100,300,100,100]


canvas.create_line(M, fill="red", width=5)

m2=eltol(M,100,-100)

canvas.create_line(m2, fill="purple", width=5)

m3=nagyit(M,10)














win.mainloop()
