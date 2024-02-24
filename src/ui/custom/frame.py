
import customtkinter as ctk


class ANFrame(ctk.CTkFrame):
    """
    Frame base class that automatically saves the engine as a weak reference.
    """
    
    def __init__(self, master):
          
        super().__init__(master)

        self._load_subviews()
    
    def _load_subviews(self):
        pass