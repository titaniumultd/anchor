
from pynput.mouse import Controller as MouseController

from src.common.interfaces.engine_interface import ANEngineInterface
from src.common.interfaces.controllers.anchor_controller_interface import ANAnchorControllerInterface
from src.common.interfaces.controllers.state_controller_interface import ANStateControllerInterface
from src.common.interfaces.config_model_interface import ANConfigModelInterface

from src.common.config_model import ANConfigModel
from src.engine.anchor_controller import ANAnchorController
from src.engine.state_controller import ANStateController


class ANEngine(ANEngineInterface, object):
    """
    Class containing all internal business logic.
    """

    def __init__(self):
        self._mouse_controller = MouseController()
        self._state_controller:ANStateControllerInterface = ANStateController(self)
        self._anchor_controller:ANAnchorControllerInterface = ANAnchorController(self)
        self._config_model:ANConfigModelInterface = ANConfigModel()

    def get_anchor_controller(self) -> ANAnchorControllerInterface:
        return self._anchor_controller

    def get_state_controller(self) -> ANStateControllerInterface:
        return self._state_controller

    def get_mouse_controller(self) -> MouseController:
        return self._mouse_controller
    
    def get_config_model(self) -> ANConfigModelInterface:
        return self._config_model

    def update(self):
        self._state_controller.update_state()