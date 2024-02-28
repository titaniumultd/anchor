
from src.common.interfaces.engine_interface import ANEngineInterface
from src.common.interfaces.controllers.anchor_controller_interface import ANAnchorControllerInterface
from src.common.interfaces.controllers.state_controller_interface import ANStateControllerInterface
from src.common.interfaces.controllers.keyboard_controller_interface import ANKeyboardControllerInterface
from src.common.interfaces.controllers.mouse_controller_interface import ANMouseControllerInterface


from src.common.config_model import ANConfigModel
from src.engine.anchor_controller import ANAnchorController
from src.engine.mouse_controller import ANMouseController
from src.engine.state_controller import ANStateController
from src.engine.keyboard_controller import ANKeyboardController

class ANEngine(ANEngineInterface, object):
    """
    Class containing all internal business logic.
    """

    def __init__(self):
        self._mouse_controller = ANMouseController()
        self._keyboard_controller = ANKeyboardController()
        self._state_controller = ANStateController(self)
        self._anchor_controller = ANAnchorController(self)
        self._config_model = ANConfigModel()

    def get_anchor_controller(self) -> ANAnchorControllerInterface:
        return self._anchor_controller

    def get_state_controller(self) -> ANStateControllerInterface:
        return self._state_controller

    def get_mouse_controller(self) -> ANMouseControllerInterface:
        return self._mouse_controller
    
    def get_keyboard_controller(self) -> ANKeyboardControllerInterface:
        return self._keyboard_controller
    
    def get_config_model(self) -> ANConfigModel:
        return self._config_model

    def update(self):
        self._state_controller.update_state()