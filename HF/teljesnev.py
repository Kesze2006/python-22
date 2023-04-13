from tkinter import *

win=Tk()

win.geometry("1100x500")

canvas=Canvas(win, width=500, height=300,bg="skyblue")
canvas.pack(fill = BOTH, expand =1)




#canvas.create_line(250,0,250,500, fill="blue", width=5)
#canvas.create_line(500,0,500,500, fill="blue", width=5)
#canvas.create_line(750,0,750,500, fill="blue", width=5)


#Á
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



win.mainloop()
