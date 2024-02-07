
import weakref

import customtkinter as ctk

from src.common.interfaces.engine_interface import ANEngineInterface


class ANFrame(ctk.CTkFrame):
    """
    Frame base class that automatically saves the engine as a weak reference.
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