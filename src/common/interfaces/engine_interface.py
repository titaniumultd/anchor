
from abc import ABC, abstractmethod

from src.common.interfaces.controllers.anchor_controller_interface import ANAnchorControllerInterface
from src.common.interfaces.controllers.keyboard_controller_interface import ANKeyboardControllerInterface
from src.common.interfaces.controllers.state_controller_interface import ANStateControllerInterface
from src.common.interfaces.controllers.mouse_controller_interface import ANMouseControllerInterface

from src.common.config_model import ANConfigModel


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
    def get_anchor_controller(self) -> ANAnchorControllerInterface:
        pass

    @abstractmethod
    def get_state_controller(self) -> ANStateControllerInterface:
        pass

    @abstractmethod
    def get_mouse_controller(self) -> ANMouseControllerInterface:
        pass

    @abstractmethod
    def get_keyboard_controller(self) -> ANKeyboardControllerInterface:
        pass

    @abstractmethod
    def get_config_model(self) -> ANConfigModel:
        pass

    @abstractmethod
    def update(self) -> None:
        pass