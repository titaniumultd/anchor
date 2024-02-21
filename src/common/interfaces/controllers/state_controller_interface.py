
from abc import ABC, abstractmethod


class ANStateControllerInterface(ABC):
    """
    Interface declaration for the state controller.
    """

    @abstractmethod
    def get_state(self) -> dict:
        pass

    @abstractmethod
    def update_state(self, key: str, value) -> None:
        pass
   