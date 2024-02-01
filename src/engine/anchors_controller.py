import weakref

from src.common.anchor import ANAnchor
from src.common.config import MAX_ANCHORS
from src.common.interfaces.engine_interface import ANEngineInterface
from src.common.interfaces.anchors_interface import ANAnchorsControllerInterface
from src.common.interfaces.state_interface import ANStateControllerInterface


class ANAnchorsController(ANAnchorsControllerInterface, object):
    """
    Manages anchors. To-Do: Separate Anchors from UI
    """

    def __init__(self, 
                 engine: ANEngineInterface):
        self._engine = weakref.ref(engine)
        self._anchors = []

    # Public Methods

    def load_anchors(self) -> list:
        while len(self._anchors) < MAX_ANCHORS:
            self._drop_an_anchor()

    def get_anchors(self) -> list:
        return self._anchors
    
    def save_anchors(self) -> None:
        pass

    # Private Methods

    def _get_root(self):
        return self._engine().get_root()
    
    def _get_mouse(self):
        return self._engine().get_mouse()
    
    def _get_notifier(self):
        return self._engine().get_notifier()

    def _get_state_controller(self) -> ANStateControllerInterface:
        return self._engine().get_state_controller()

    def _drop_an_anchor(self):
        # to-do: clean-up
        if len(self._anchors) >= MAX_ANCHORS:
            return
        
        new_anchor = ANAnchor(len(self._anchors), self._engine())
        self._anchors.append(new_anchor)
        self.save_anchors()
    