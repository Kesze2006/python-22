from tkinter import *

win=Tk()

win.geometry("700x350")

canvas=Canvas(win, width=500, height=300, bg = "purple")
canvas.pack(fill = BOTH)

canvas.create_line(200,250,300,100,325,100,400,250,350,250,315,175,300,175,250,250,200,250, fill="blue", width=5)
canvas.create_line(295,150,310,125,325,150,295,150,fill="blue", width=5)
canvas.create_line(315,75,330,50,345,60,330,85,315,75, fill="blue", width=5)

win.mainloop()
