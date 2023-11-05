import tkinter as tk
from src.Global.Colours import *


class Checkbutton(tk.Checkbutton):
    def __init__(self, master=None, cnf={}, **kw):
        super().__init__(master, cnf, **kw)
        self.configure(
            background=BACKGROUND_COLOUR,
            activebackground=BACKGROUND_COLOUR,
            foreground=TEXT_COLOUR,
            activeforeground=TEXT_COLOUR,
            relief='flat',
            borderwidth=0,
        )
