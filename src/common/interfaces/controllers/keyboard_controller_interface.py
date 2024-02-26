
from abc import ABC, abstractmethod

class ANKeyboardControllerInterface(ABC):
    
    @abstractmethod
    def record_hotkey(self) -> str:
        pass