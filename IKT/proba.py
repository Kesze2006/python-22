from tkinter import *
ablak=Tk()

ablak.geometry("400x400")

ablak.title("Amőba játék")

ablak.configure(bg="blue")

szoveg= Canvas(ablak, bg="red", width= 100,height= 50)
szoveg.create_text(50,25,text="Próba cumó",fill="black")
szoveg.pack()


ablak.mainloop()
