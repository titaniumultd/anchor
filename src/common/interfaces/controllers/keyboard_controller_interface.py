
from abc import ABC, abstractmethod


class ANKeyboardControllerInterface(ABC):
    
    @abstractmethod
    def record_hotkey(self) -> str:
        pass

    @abstractmethod
    def set_hotkey(self, hotkey:str, action:callable):
        pass

    @abstractmethod
    def clear_hotkey(self, hotkey:str):
        pass