
from abc import ABC, abstractmethod

class ANTrayViewInterface(ABC):

    @abstractmethod
    def update(self, packet: dict):
        pass
