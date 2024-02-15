
from abc import ABC, abstractmethod

from src.common.interfaces.anchors_interface import ANAnchorsControllerInterface
from src.common.interfaces.profile_interface import ANProfileControllerInterface
from src.common.interfaces.state_interface import ANStateControllerInterface


class ANEngineInterface(ABC):
    """
    Interface declaration for the engine.

    The engine should contain all internal business logic, separated into controllers.
    
    Public methods to engine and controller classes should be defined in an interface so that we don't
    need to reference their respective class directly, therefore keeping dependencies clean.

    Example:
                                     Engine
    |--------|        via         |--------------------------------------------------------|
    |  View  |      ------>       |                           via                          |
    |--------|  Engine Interface  |  Profile Controller  <------------>  State Controller  |
                                  |                         Interface                      |
                                  |--------------------------------------------------------|
    """

    @abstractmethod
    def get_anchors_controller(self) -> ANAnchorsControllerInterface:
        pass

    @abstractmethod
    def get_profile_controller(self) -> ANProfileControllerInterface:
        pass

    @abstractmethod
    def get_state_controller(self) -> ANStateControllerInterface:
        pass
    
    '''    @abstractmethod
    def get_root(self): # to-do: Add typing
        pass'''

    @abstractmethod
    def get_mouse(self): # to-do: Add typing
        pass

    @abstractmethod
    def get_notifier(self): # to-do: Add typing
        pass

    @abstractmethod
    def load(self) -> None:
        pass