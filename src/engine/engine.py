
from pynput.mouse import Controller as MouseController

from src.common.interfaces.engine_interface import ANEngineInterface
from src.common.notifier import ANNotifyListener, ANNotifier

from src.engine.anchors_controller import ANAnchorsController
from src.engine.profile_controller import ANProfileController
from src.engine.state_controller import ANStateController
from src.engine.view_model import ANViewModel

class ANEngine(ANEngineInterface, ANNotifyListener, object):
    """
    Class containing all internal business logic.
    """

    def __init__(self, root):
        self._root = root
        
        self._mouse = MouseController()
        self._state_controller = ANStateController()
        self._profile_controller = ANProfileController(self)
        self._anchors_controller = ANAnchorsController(self)
        self._view_model = None

    def get_anchors_controller(self):
        return self._anchors_controller

    def get_profile_controller(self):
        return self._profile_controller

    def get_state_controller(self):
        return self._state_controller
    
    def get_view_model(self):
        return self._view_model
    
    def get_root(self):
        return self._root

    def get_mouse(self):
        return self._mouse

    def get_notifier(self):
        return self._notifier

    def load(self) -> None:
        self._state_controller.load_state()
        self._profile_controller.load_profiles()
        self._anchors_controller.load_anchors()
        self._view_model = ANViewModel(self._root, self)

    # ANNotifyListener
        
    def update(self):
        self.get_anchors_controller().save_anchors()
    