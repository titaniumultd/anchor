
from pynput.mouse import Controller as MouseController

from src.common.interfaces.engine_interface import ANEngineInterface
from src.common.interfaces.ui.config_view_model_interface import ANConfigViewModelInterface
from src.common.interfaces.ui.tray_view_model_interface import ANTrayViewModelInterface
from src.common.interfaces.controllers.anchor_controller_interface import ANAnchorControllerInterface
from src.common.interfaces.controllers.profile_controller_interface import ANProfileControllerInterface
from src.common.interfaces.controllers.state_controller_interface import ANStateControllerInterface

from src.common.config_model import ANConfigModel
from src.engine.anchor_controller import ANAnchorController
from src.engine.profile_controller import ANProfileController
from src.engine.state_controller import ANStateController
from src.ui.tray.tray_view_model import ANTrayViewModel
from src.ui.config.config_view_model import ANConfigViewModel


class ANEngine(ANEngineInterface, object):
    """
    Class containing all internal business logic.
    """

    def __init__(self):
        self._mouse_controller = MouseController()
        self._state_controller:ANStateControllerInterface = ANStateController()
        self._profile_controller:ANProfileControllerInterface = ANProfileController(self)
        self._anchors_controller:ANAnchorControllerInterface = ANAnchorController(self)
        self._config_model:ANConfigModelInterface = ANConfigModel()

        self._config_view_model:ANConfigViewModelInterface = None
        self._tray_view_model:ANTrayViewModelInterface = None

    def get_anchors_controller(self) -> ANAnchorControllerInterface:
        return self._anchors_controller

    def get_profile_controller(self) -> ANProfileControllerInterface:
        return self._profile_controller

    def get_state_controller(self) -> ANStateControllerInterface:
        return self._state_controller

    def get_mouse_controller(self) -> MouseController:
        return self._mouse_controller

    def load(self) -> None:
        self._state_controller.load_state()
        self._profile_controller.load_profiles()
        self._anchors_controller.load_anchors()

        self._load_ui()

    def mainloop(self):
        while running:
            self._view_models.update()
            sleep()

    def _load_ui(self):
        self._config_view_model = ANConfigViewModel(self._config_model, self._anchors_controller)
        self._tray_view_model = ANTrayViewModel(self)