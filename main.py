from tkinter import *
from functools import partial
import tkinter as tk, threading
from PIL import Image, ImageTk

video_dir = r"video/robot.mp4"


class PlayPauseButton:
    def __init__(self, play_pause, image_button):

        fr = Frame(app)
        fr.place(x=20, y=430)

        Button(fr, image=image_button, command=partial(self.change_state, fr, play_pause)).grid(row=2, column=2)

    def change_state(self, fr, play_pause):
        fr.destroy()

        if play_pause == "play":
            PlayPauseButton("pause", iPause)
        else:
            PlayPauseButton("play", iPlay)


def stop_state():
    print("stoooppp")


def faster_state():
    print("fassstterrr")


def start_state():
    print("go to starrttt")


if __name__ == "__main__":
    app = Tk()

    app.title("TardisPlayer")
    app.geometry('1000x500')

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
    start_button = Button(app, height=70, image=iStart, command=start_state).place(x=840, y=430)
    faster_button = Button(app, image=iFaster, command=faster_state).place(x=900, y=430)

    app.mainloop()
