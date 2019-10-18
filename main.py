from tkinter import *
from tkinter.ttk import *

# creating tkinter window
root = Tk()

root.title("TardisPlayer")
root.geometry('1000x500')

screen = Frame(height=420, relief=SUNKEN)
screen.pack(fill=X, padx=5, pady=5)

photoPlay = PhotoImage(file=r"images/play.png")
photoPause = PhotoImage(file=r"images/pause.png")
photoStop = PhotoImage(file=r"images/stop.png")

iPlay = photoPlay.subsample(2, 2)
iPause = photoPause.subsample(2, 2)
iStop = photoStop.subsample(2, 2)

play = Button(root, image=iPlay).place(x=10, y=450)
pause = Button(root, image=iPause).place(x=100, y=450)
stop = Button(root, image=iStop).place(x=190, y=450)



root.mainloop()
