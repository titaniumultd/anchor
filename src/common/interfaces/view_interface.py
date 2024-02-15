
from abc import ABC, abstractmethod

from customtkinter import CTk


class ANViewInterface(ABC):

    @abstractmethod
    def get_root(self) -> CTk:
        pass
    
    @abstractmethod
    def load(self):
        pass

    @abstractmethod
    def show_window(self):
        pass
    
    @abstractmethod
    def hide_window(self):
        pass
    
    @abstractmethod
    def exit(self):
        pass
    
    @abstractmethod
    def toggle_hotkeys(self):
        pass