from tkinter import *
import pydot
# pip install pillow
from PIL import Image, ImageTk

from frontend import graphs


def resizeImage(width, img):
    wpercent = (width / float(img.size[0]))
    hsize = int((float(img.size[1]) * float(wpercent)))
    img = img.resize((width, hsize), Image.ANTIALIAS)
    return img


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
        load = resizeImage(600, Image.open(graphs.graf()))
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.image = render
        img.pack()


def makeWindow():
    root = Tk()
    app = Window(root)
    root.wm_title("Network Traffic Monitor")
    root.mainloop()
