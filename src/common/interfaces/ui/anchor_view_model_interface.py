
from abc import ABC, abstractmethod
import customtkinter as ctk


class ANAnchorViewModelInterface(ABC):
    def __init__(self):
        self.record_hotkey_strvar:ctk.StringVar
        self.click_hotkey_strvar:ctk.StringVar
        self.anchor_action:str
    
    @abstractmethod
    def update(self):
        pass
    
    @abstractmethod
    def update_action(self, action:str):
        pass

    @abstractmethod
    def request_hotkey_update(self, hotkey:str):
        pass