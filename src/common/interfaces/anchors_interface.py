
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

    @abstractmethod
    def save_anchors(self) -> None:
        pass

    @abstractmethod
    def activate_hotkeys(self) -> None:
        """
        Activates hotkeys for all loaded anchors.
        """
        pass