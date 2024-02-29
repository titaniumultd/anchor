

from abc import ABC, abstractmethod

class ANConfigModelInterface(ABC):

    @abstractmethod
    def toggle_global_hotkey_state(self) -> bool:
        pass
    
    @abstractmethod
    def get_global_hotkey_state(self) -> bool:
        pass