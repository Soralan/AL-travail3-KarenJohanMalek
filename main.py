import my_video
from tkinter import *
from functools import partial
import tkinter as tk, threading
from PIL import Image, ImageTk
from tkinter import filedialog


class PlayPauseButton:
    def __init__(self, play_pause, image_button):

        fr = Frame(app)
        fr.place(x=50, y=20)

        Button(fr, image=image_button, command=partial(self.change_state, fr, play_pause)).grid(row=2, column=2)

    def change_state(self, fr, play_pause):
        fr.destroy()

        if play_pause == "play":
            PlayPauseButton("pause", iPause)
        else:
            PlayPauseButton("play", iPlay)
        my_video.playPause(video)


def faster_state():
    print("fassstterrr")
    my_video.acceleration(video)


def aFile():
    app.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("avi files","*.avi"),("all files","*.*")))
    tmp=app.filename
    fo = open("foo.txt", "w")
    fo.write(tmp)
    fo.close()
    video = my_video.openVideo()
	
def start_state():
    print("go to starrttt")
    my_video.goBackToStart(video)


if __name__ == "__main__":
    app = Tk()

    app.title("SOPlayer")
    app.geometry('400x100')

    # create button images
    open_iPlay = Image.open("images/play.png")
    open_iPause = Image.open("images/pause.png")
    open_iFaster = Image.open("images/faster.png")
    open_iStart = Image.open("images/go_back.png")

    iPause = ImageTk.PhotoImage(open_iPause)
    iPlay = ImageTk.PhotoImage(open_iPlay)
    iFaster = ImageTk.PhotoImage(open_iFaster)
    iStart = ImageTk.PhotoImage(open_iStart)

    # create buttons
    PlayPauseButton("play", iPlay)
    start_button = Button(app, height=65, image=iStart, command=start_state).place(x=240, y=20)
    faster_button = Button(app, image=iFaster, command=faster_state).place(x=320, y=20)
    name_File=Button(app,height=3, text="Choose", command=aFile).place(x=150, y=18)
    aFile()
    video = my_video.openVideo()
	
	
	

    app.mainloop()
