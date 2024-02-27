
import threading
import weakref

from src.common.anchor_model import ANAnchor
from src.common.variables import MAX_ANCHORS
from src.common.interfaces.engine_interface import ANEngineInterface
from src.common.interfaces.controllers.anchor_controller_interface import ANAnchorControllerInterface
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
    
    def update_hotkey(self, anchor:ANAnchorModelInterface, hotkey_type:str, callback:callable):
        threading.Thread(target=self._new_hotkey_threaded, args=(anchor, hotkey_type, callback)).start()
    
    def _create_new_anchor(self):
        new_anchor = ANAnchor()
        self._anchors.append(new_anchor)

    def _init_anchors(self):
        state = self._engine().get_state_controller().get_state()

        if state is not None:
            for anchor_dict in state:
                self._load_anchor_from_state(state[anchor_dict])

        while len(self._anchors) < MAX_ANCHORS:
            self._create_new_anchor()

    def _load_anchor_from_state(self,  anchor_dict: dict):
        anchor = ANAnchor()

        anchor.set_hotkey('record', anchor_dict.get('record_hotkey'))
        anchor.set_hotkey('click', anchor_dict['click_hotkey'])
        anchor.set_anchor_position(anchor_dict['mouse_position'])
        anchor.set_action(anchor_dict['action'])

        self._anchors.append(anchor)

    def _new_hotkey_threaded(self, anchor:ANAnchorModelInterface, hotkey_type:str, callback:callable):
        new_hotkey = self._engine().get_keyboard_controller().record_hotkey()
        anchor.set_hotkey(hotkey_type, new_hotkey)
        self._engine().update()
        callback()