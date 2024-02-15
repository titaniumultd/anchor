from abc import abstractmethod

from customtkinter import CTkFrame

class ANFrameInterface(CTkFrame):

    @abstractmethod
    def get_view(self):
        pass
    
    def load_subviews(self):
        pass