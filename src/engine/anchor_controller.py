
import logging
import weakref

from src.common.anchor_model import ANAnchor
from src.common.variables import MAX_ANCHORS
from src.common.interfaces.engine_interface import ANEngineInterface
from src.common.interfaces.controllers.anchor_controller_interface import ANAnchorControllerInterface
from src.common.interfaces.controllers.state_controller_interface import ANStateControllerInterface
from src.common.interfaces.anchor_model_interface import ANAnchorModelInterface


class ANAnchorController(ANAnchorControllerInterface, object):
    """
    Manages anchors
    """

    def __init__(self, 
                 engine: ANEngineInterface):
        self._engine = weakref.ref(engine)
        self._anchors = []

        self._init_anchors()

    def get_anchors(self) -> list[ANAnchorModelInterface]:
        return self._anchors

    def _get_state_controller(self) -> ANStateControllerInterface:
        return self._engine().get_state_controller()
    
    def _create_new_anchor(self):
        new_anchor = ANAnchor()
        self._anchors.append(new_anchor)

    def _load_anchor_from_state(self,  anchor_dict: dict):
        anchor = ANAnchor()

        anchor.set_hotkey('record', anchor_dict.get('record_hotkey'))
        anchor.set_hotkey('click', anchor_dict['click_hotkey'])
        anchor.set_anchor_position(anchor_dict['mouse_position'])
        anchor.set_action(anchor_dict['action'])

        self._anchors.append(anchor)
    
    def _get_engine(self) -> ANEngineInterface:
        return self._engine()
    
    def _init_anchors(self):
        state = self._get_state_controller().get_state()

        if state is not None:
            for anchor_dict in state:
                self._load_anchor_from_state(state[anchor_dict])

        while len(self._anchors) < MAX_ANCHORS:
            self._create_new_anchor()