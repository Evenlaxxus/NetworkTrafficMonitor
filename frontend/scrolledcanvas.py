from tkinter import *

from PIL import Image, ImageTk
from frontend import graphs


class ScrolledCanvas(Frame):
    def __init__(self, scan_type, file='', parent=None):
        Frame.__init__(self, parent)
        self.master.title("Spectrogram Viewer")
        self.pack(expand=YES, fill=BOTH)
        canv = Canvas(self, relief=SUNKEN)
        canv.config(width=400, height=200)
        canv.config(highlightthickness=0)
        sbarV = Scrollbar(self, orient=VERTICAL)
        sbarH = Scrollbar(self, orient=HORIZONTAL)
        sbarV.config(command=canv.yview)
        sbarH.config(command=canv.xview)
        canv.config(yscrollcommand=sbarV.set)
        canv.config(xscrollcommand=sbarH.set)
        sbarV.pack(side=RIGHT, fill=Y)
        sbarH.pack(side=BOTTOM, fill=X)
        canv.pack(side=LEFT, expand=YES, fill=BOTH)
        self.im = Image.open(graphs.graph(scan_type, file))
        width, height = self.im.size
        canv.config(scrollregion=(0, 0, width, height))
        self.im2 = ImageTk.PhotoImage(self.im)
        self.imgtag = canv.create_image(0, 0, anchor="nw", image=self.im2)
