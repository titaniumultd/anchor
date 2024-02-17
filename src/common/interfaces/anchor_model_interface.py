
from abc import ABC, abstractmethod


class ANAnchorModelInterface(ABC):

    @abstractmethod
    def get_position(self) -> tuple[int,int]:
        pass
    
    @abstractmethod
    def get_action(self) -> str:
        pass
    
    @abstractmethod
    def get_hotkey(self, hotkey_type: str) -> str:
        pass
    
    @abstractmethod
    def set_anchor_position(self, position: tuple[int,int]):
        '''
        Returns the stored mouse position the anchor will activate
        '''
        pass
    
    @abstractmethod
    def set_hotkey(self, hotkey_type: str, key_combo: str):
        pass
    
    @abstractmethod
    def set_action(self, action: str):
        pass