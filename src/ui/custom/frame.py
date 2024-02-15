
import weakref

import customtkinter as ctk


class ANFrame(ctk.CTkFrame):
    """
    Frame base class that automatically saves the engine as a weak reference.
    """
    
    def __init__(self, 
                 root: ctk.CTk,
                 view
                 ):
        super().__init__(root)
        
        self._root = weakref.ref(root)
        self._view = weakref.ref(view)

        self.load_subviews()

    def get_root(self):
        return self._root()
    
    def get_view(self):
        return self._view()
    
    def load_subviews(self):
        pass