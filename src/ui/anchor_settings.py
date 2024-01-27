
import tkinter as tk

class ANAnchorSettings(tk.Frame):
    """
    Top level anchor settings view container. Should contain a list of anchors, editable by the user.
    """
    def __init__(self, master):
        super().__init__(master)
        
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.pack()

        