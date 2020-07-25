from tkinter import *
import pydot
# pip install pillow
from PIL import Image, ImageTk

from frontend import graphs


class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.pack(fill=BOTH, expand=1)
        self.generate = Button(self)
        self.generate["text"] = "Generate graph"
        self.generate["fg"] = "red"
        self.generate["command"] = self.generateGraph
        self.generate.pack()

    def generateGraph(self):
        load = Image.open(graphs.graf())
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.image = render
        img.place(x=50, y=50)


def makeWindow():
    root = Tk()
    app = Window(root)
    root.wm_title("Network Traffic Monitor")
    root.geometry("1024x768")
    root.mainloop()
