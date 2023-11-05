import tkinter as tk
from src.Global.Colours import BUTTON_COLOUR


class Separator(tk.Frame):
    def __init__(self, master=None, cnf={}, **kw):
        super().__init__(master, cnf, **kw)
        self.configure(
            background=BUTTON_COLOUR,
            height=1,
            bd=0
        )
