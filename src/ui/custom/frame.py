
import weakref

import customtkinter as ctk

from src.common.interfaces.view_interface import ANViewInterface


class ANFrame(ctk.CTkFrame):
    """
    Frame base class that automatically saves the engine as a weak reference.
    """
    
    def __init__(self, 
                 master,
                 view: ANViewInterface):
        super().__init__(master)
        
        self._view = weakref.ref(view)
        
        self.load_subviews()

    def get_view(self):
        return self._view()
    
    def load_subviews(self):
        pass