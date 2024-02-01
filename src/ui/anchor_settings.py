
import weakref
import tkinter as tk

from src.common.interfaces.engine_interface import ANEngineInterface

class ANAnchorSettings(tk.Frame):
    """
    Top level anchor settings view container. Should contain a list of anchors, editable by the user.
    """
    def __init__(self, 
                 master,
                 engine: ANEngineInterface):
        super().__init__(master)
        
        self._engine = weakref.ref(engine)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        