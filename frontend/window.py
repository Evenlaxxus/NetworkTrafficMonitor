from tkinter import *
from PIL import Image, ImageTk

from frontend import graphs
from frontend import scrolledcanvas


def resizeImage(width, img):
    ratio = (width / float(img.size[0]))
    height = int((float(img.size[1]) * float(ratio)))
    img = img.resize((width, height), Image.ANTIALIAS)
    return img


def makeWindow():
    root = Tk()
    app = Window(root)
    root.wm_title("Network Traffic Monitor")
    root.mainloop()


def generateGraphFromFile():
    scrolledcanvas.ScrolledCanvas('file').mainloop()


def generateGraphFromLiveCapture():
    scrolledcanvas.ScrolledCanvas('live').mainloop()


class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.pack(fill=BOTH, expand=1)
        self.generate_from_file = Button(self)
        self.generate_from_file["text"] = "Generate graph from file"
        self.generate_from_file["fg"] = "red"
        self.generate_from_file["command"] = generateGraphFromFile
        self.generate_from_file.pack(side=LEFT)
        self.generate_from_scan = Button(self)
        self.generate_from_scan["text"] = "Generate graph from live capture"
        self.generate_from_scan["fg"] = "red"
        self.generate_from_scan["command"] = generateGraphFromLiveCapture
        self.generate_from_scan.pack(side=LEFT)
