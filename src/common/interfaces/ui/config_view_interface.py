

from abc import ABC, abstractmethod

class ANConfigViewInterface(ABC):

    @abstractmethod
    def update(self, update_packet: dict):
        pass
