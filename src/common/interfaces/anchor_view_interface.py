
from abc import ABC, abstractmethod

from src.ui.custom.frame import ANFrame

class ANAnchorViewInterface(ABC, ANFrame):

    @abstractmethod
    def update(self,
               anchor_index:int,
               record_combo:str, 
               click_combo:str, 
               action:str
               ):
        pass