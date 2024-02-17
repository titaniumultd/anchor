
from abc import ABC, abstractmethod

from src.common.interfaces.anchor_model_interface import ANAnchorModelInterface


class ANAnchorsControllerInterface(ABC):
    """
    Interface declaration for the anchors controller.
    """

    @abstractmethod
    def load_anchors(self) -> list:
        pass

    @abstractmethod
    def get_anchors(self) -> list[ANAnchorModelInterface]:
        """
        Returns the anchors in a list.
        """
        pass

    @abstractmethod
    def save_anchors(self) -> None:
        pass

    @abstractmethod
    def get_hotkeys_enabled_state(self) -> bool:
        pass

    @abstractmethod
    def disable_all_hotkeys(self):
        pass

    @abstractmethod
    def enable_all_hotkeys(self):
        pass