import tkinter as tk
from tkinter.ttk import Notebook
from window.running import running
from window.images import images
from window.version import version


class Tk(tk.Tk):
    w = 700
    h = 400

    def __init__(self):
        super(Tk, self).__init__()
        self.title("docker简易管理")
        ws = self.winfo_screenwidth()
        hs = self.winfo_screenheight()
        self.x = (ws / 2) - (self.w / 2)
        self.y = (hs / 2) - (self.h / 2)
        self.geometry('%dx%d+%d+%d' % (self.w, self.h, self.x, self.y))
        self.handel()

    def handel(self):
        notebook = Notebook(self)
        running_tab = running(notebook)
        images_tab = images(notebook)
        version_tab = version(notebook)

        notebook.add(running_tab, text=running.title)
        notebook.add(images_tab, text=images.title)
        notebook.add(version_tab, text=version.title)
        notebook.pack(fill=tk.BOTH, expand=1)
