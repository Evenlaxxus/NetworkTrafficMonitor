from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog

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


class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.filename = ''
        self.master = master
        self.pack(fill=BOTH, expand=1)
        self.generate_from_file = Button(self)
        self.generate_from_file["text"] = "Generate graph from file"
        self.generate_from_file["command"] = self.generateGraphFromFile
        self.generate_from_file.pack(side=LEFT)

        self.generate_from_scan = Button(self)
        self.generate_from_scan["text"] = "Generate graph from live capture"
        self.generate_from_scan["command"] = self.generateGraphFromLiveCapture
        self.generate_from_scan.pack(side=LEFT)

    def generateGraphFromFile(self):
        self.filename = filedialog.askopenfilename(initialdir='c:/', title='Choose pcap file',
                                                   filetypes=(('pcap files', '*.pcap'), ('all files', '*.*')))
        scrolledcanvas.ScrolledCanvas('file', self.filename).mainloop()

    def generateGraphFromLiveCapture(self):
        scrolledcanvas.ScrolledCanvas('live').mainloop()
