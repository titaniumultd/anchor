
import customtkinter as ctk


class ANFrame(ctk.CTkFrame):
    """
    Frame base class that automatically saves the engine as a weak reference.
    """
    
    def __init__(self, root):

        super().__init__(root)

        self.load_subviews()
    
    def load_subviews(self):
        pass