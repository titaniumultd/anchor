
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

    def get_view_model(self):
        pass

    @abstractmethod
    def disable_all_hotkeys(self) -> None:
        pass

    @abstractmethod
    def enable_all_hotkeys(self) -> None:
        pass

    @abstractmethod
    def save_anchors(self) -> None:
        pass

    @abstractmethod
    def toggle_hotkeys(self) -> None:
        pass