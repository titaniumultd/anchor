
from src.common.interfaces.engine_interface import ANEngineInterface

from src.engine.anchors_controller import ANAnchorsController
from src.engine.state_controller import ANStateController


class ANEngine(ANEngineInterface, object):
    """
    Class containing all internal business logic.
    """

    def __init__(self,
                 root,
                 mouse,
                 notifier):
        # to-do: create root, mouse and notifier within engine
        self._root = root
        self._mouse = mouse
        self._notifier = notifier

        self._state_controller = ANStateController()
        self._anchors_controller = ANAnchorsController(self)

    def get_anchors_controller(self):
        return self._anchors_controller

    def get_state_controller(self):
        return self._state_controller
    
    def get_root(self):
        return self._root

    def get_mouse(self):
        return self._mouse

    def get_notifier(self):
        return self._notifier

    def load(self) -> None:
        self._state_controller.load_state()
        self._anchors_controller.load_anchors()
