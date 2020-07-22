from tkinter import *
import pydot
# pip install pillow
from PIL import Image, ImageTk


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
        (graph,) = pydot.graph_from_dot_file('graph-output/graph.gv')
        graph.write_png('graph-output/somefile.png')
        load = Image.open("graph-output/somefile.png")
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.image = render
        img.place(x=50, y=50)


def makeWindow():
    root = Tk()
    app = Window(root)
    root.wm_title("Network Traffic Monitor")
    root.geometry("400x300")
    root.mainloop()
