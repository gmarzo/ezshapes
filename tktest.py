from tkinter import Tk, Canvas
from tkinter import ttk

root = Tk()
root.geometry('700x400+350+200')
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

framerate:int = 60

def set_fps(fps: int):
    global root, framerate

    framerate = fps
#     __fps_runner()
    
# def __fps_runner():
#     root.after(1000//framerate, draw)


canvas = Canvas(root, width=700, height=400, background="grey")
canvas.grid(column=0, row=0)

def draw():
    ufox = 300
    ufox += 1
    canvas.create_rectangle(0, 0, 700, 400, fill="skyblue", outline="skyblue")
    canvas.create_rectangle(0, 350, 700, 400, fill="darkgreen", outline="darkgreen")

    canvas.create_oval(ufox, 250, ufox+100, 300, fill="gray", outline="black")
    canvas.create_oval(ufox+25, 245, ufox+75, 275, fill="lightblue", outline="black")

set_fps(60)
root.after(1000//framerate, draw)
root.mainloop()
