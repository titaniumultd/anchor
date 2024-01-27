
import tkinter as tk

from src.ui.anchor_settings import ANAnchorSettings

class ANRootView(tk.Frame):
    """
    Root view potentially containing multiple different top level views (ie. login or main anchor view).
    """
    def __init__(self, master):
        super().__init__(master)
        self.pack()

        self.anchor_settings = ANAnchorSettings(self)

        

        