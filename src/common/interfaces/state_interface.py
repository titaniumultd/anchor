
from abc import ABC, abstractmethod

class ANStateControllerInterface(ABC):
    """
    Interface declaration for the state controller.
    """

    @abstractmethod
    def load_state(self) -> None:
        """
        Load's application state and returns true if successful.
        """
        pass

    @abstractmethod
    def save_state(self) -> None:
        pass

    @abstractmethod
    def get_state(self) -> dict:
        pass
   