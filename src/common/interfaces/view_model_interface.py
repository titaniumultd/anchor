
from abc import ABC, abstractmethod

class ANViewModelInterface(ABC):
    """
    Interface declaration for ANViewModel
    """
    @abstractmethod
    def disable_all_hotkeys(self):
        pass

    def enable_all_hotkeys(self):
        pass
    
    def dither_all_buttons(self):
        pass
    
    def undither_all_buttons(self):
        pass
    
    def update_text_entry(self, component, value):
        pass
    
    def set_hotkey(self, anchor, type):
        pass

    def restore_ui(self):
        pass