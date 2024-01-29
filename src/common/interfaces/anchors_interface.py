
from abc import ABC, abstractmethod


class ANAnchorsControllerInterface(ABC):
    """
    Interface declaration for the anchors controller.
    """

    @abstractmethod
    def load_anchors(self) -> list:
        pass

    @abstractmethod
    def get_anchors(self) -> list:
        """
        Returns the anchors in a list.
        """
        pass