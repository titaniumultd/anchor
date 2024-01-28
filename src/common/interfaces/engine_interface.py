
from abc import ABC, abstractmethod

from src.common.interfaces.profile_interface import ANProfileControllerInterface
from src.common.interfaces.state_interface import ANStateControllerInterface

class ANEngineInterface(ABC):
    """
    Interface declaration for the engine.
    """

    @abstractmethod
    def get_profile_controller(self) -> ANProfileControllerInterface:
        pass

    @abstractmethod
    def get_state_controller(self) -> ANStateControllerInterface:
        pass
    