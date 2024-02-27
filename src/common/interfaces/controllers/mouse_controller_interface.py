
from abc import ABC, abstractmethod


class ANMouseControllerInterface(ABC):

    @abstractmethod
    def get_position(self) -> tuple[int, int]:
        pass
    
    def set_position(self, position: tuple[int, int]):
        pass

    def click(self, laterality:str):
        pass