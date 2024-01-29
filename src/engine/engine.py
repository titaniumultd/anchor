
from src.common.interfaces.engine_interface import ANEngineInterface

from src.engine.anchors_controller import ANAnchorsController
from src.engine.profile_controller import ANProfileController
from src.engine.state_controller import ANStateController

class ANEngine(ANEngineInterface, object):
    """
    Class containing all internal business logic.
    """

    def __init__(self):
        self._state_controller = ANStateController()
        self._profile_controller = ANProfileController(self)
        self._anchors_controller = ANAnchorsController(self)

    def get_anchors_controller(self):
        return self._anchors_controller

    def get_profile_controller(self):
        return self._profile_controller

    def get_state_controller(self):
        return self._state_controller

    def load(self) -> None:
        self._state_controller.load_state()
        self._profile_controller.load_profiles()
        self._anchors_controller.load_anchors()
    