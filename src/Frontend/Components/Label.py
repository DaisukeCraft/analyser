import tkinter as tk
from src.Global.Colours import *


class Label(tk.Label):
    def __init__(self, master=None, cnf={}, **kw):
        super().__init__(master, cnf, **kw)
        self.configure(
            background=BACKGROUND_COLOUR,
            relief='flat',
            foreground=TEXT_COLOUR
        )
