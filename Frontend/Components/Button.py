import tkinter as tk
from Global.Colours import *


class Button(tk.Button):
    def __init__(self, master=None, cnf={}, **kw):
        super().__init__(master, cnf, **kw)
        self.configure(
            background=TEXT_COLOUR,
            activebackground=BACKGROUND_COLOUR,
            foreground=BACKGROUND_COLOUR,
            activeforeground=TEXT_COLOUR,
            relief='ridge',
            bd=1
        )
