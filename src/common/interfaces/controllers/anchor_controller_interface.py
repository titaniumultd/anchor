
from abc import ABC, abstractmethod

from src.common.anchor_model import ANAnchor


class ANAnchorControllerInterface(ABC):
    """
    Interface declaration for the anchors controller.
    """

    @abstractmethod
    def get_anchors(self) -> list[ANAnchor]:
        """
        Returns the anchors in a list.
        """
        pass
