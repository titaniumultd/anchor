
from abc import ABC, abstractmethod
import customtkinter as ctk


class ANAnchorViewModelInterface(ABC):
    
    @property
    def record_hotkey_strvar(self) -> ctk.StringVar:
        pass
    
    @property
    def click_hotkey_strvar(self) -> ctk.StringVar:
        pass
    
    @abstractmethod
    def update(self):
        pass
    
    @abstractmethod
    def update_action(self, action:str):
        pass

    @abstractmethod
    def request_hotkey_update(self, hotkey:str):
        pass