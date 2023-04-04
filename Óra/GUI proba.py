from tkinter import *
win=Tk()

# Set the size of the tkinter window
win.geometry("700x500+500+500")

# Create a canvas widget
canvas=Canvas(win, width=500, height=300, bg="green")
canvas.pack(fill = BOTH, expand = 1)

#canvas2=Canvas(win, width=500, height=300, bg="skyblue")
#canvas2.pack(fill = BOTH, expand = 1)
# Add a line in canvas widget
canvas.create_line(100,100,300,100,300,300,100,300,100,100, fill="red", width=10)
canvas.create_line(300,300,150,300,300,300, fill="blue", width=10)

win.mainloop()
