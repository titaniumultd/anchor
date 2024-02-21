
from abc import ABC, abstractmethod

from src.common.interfaces.anchor_model_interface import ANAnchorModelInterface


class ANAnchorControllerInterface(ABC):
    """
    Interface declaration for the anchors controller.
    """

    @abstractmethod
    def get_anchors(self) -> list[ANAnchorModelInterface]:
        """
        Returns the anchors in a list.
        """
        pass
