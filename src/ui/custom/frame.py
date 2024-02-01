
import weakref
import tkinter as tk

from src.common.interfaces.engine_interface import ANEngineInterface

class ANFrame(tk.Frame):
    """
    Top level anchor settings view container. Should contain a list of anchors, editable by the user.
    """
    
    def __init__(self, 
                 master,
                 engine: ANEngineInterface):
        super().__init__(master)
        
        self._engine = weakref.ref(engine)

        self.load_subviews()

    def get_engine(self):
        return self._engine()
    
    def load_subviews(self):
        pass