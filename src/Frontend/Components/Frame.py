import tkinter as tk
from src.Global.Colours import BACKGROUND_COLOUR


class Frame(tk.Frame):
    def __init__(self, master=None, cnf={}, **kw):
        super().__init__(master, cnf, **kw)
        self.configure(
            background=BACKGROUND_COLOUR
        )
