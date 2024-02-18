
from abc import ABC, abstractmethod


class ANAnchorViewModelInterface(ABC):
    
    @abstractmethod
    def update(self,
               anchor_index:int,
               record_combo:str, 
               click_combo:str, 
               action:str
               ):
        pass

    def update_action(self, action:str):
        pass

    def request_hotkey_update(self, hotkey:str):
        pass