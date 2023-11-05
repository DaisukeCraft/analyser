from tkinter import ttk
from src.Global.Colours import *


class Combobox(ttk.Combobox):
    def __init__(self, master=None, **kw):
        super().__init__(master, **kw)
        self.configure(
            foreground=TEXT_COLOUR,
            background=BACKGROUND_COLOUR,
            state='readonly'
        )
