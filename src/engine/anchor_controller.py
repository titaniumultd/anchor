
import threading
import weakref

from src.common.anchor_model import ANAnchor
from src.common.variables import MAX_ANCHORS
from src.common.interfaces.engine_interface import ANEngineInterface
from src.common.interfaces.controllers.anchor_controller_interface import ANAnchorControllerInterface


class ANAnchorController(ANAnchorControllerInterface, object):
    """
    Manages anchors
    """

    def __init__(self, 
                 engine: ANEngineInterface):
        self._engine = weakref.ref(engine)
        self._anchors:list[ANAnchor] = []

        self._init_anchors()

    def get_anchors(self) -> list[ANAnchor]:
        return self._anchors
    
    def update_hotkey(self, anchor:ANAnchor, hotkey_type:str, callback:callable):
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
        
        anchor.set_anchor_position(anchor_dict['mouse_position'])
        anchor.set_action(anchor_dict['action'])

        if anchor_dict.get('record_hotkey') != 'undefined':
            anchor.set_hotkey('record', anchor_dict['record_hotkey'])
            self._bind_record(anchor)

        if anchor_dict.get('click_hotkey') != 'undefined':
            anchor.set_hotkey('click', anchor_dict['click_hotkey'])
            self._bind_click(anchor)

        self._anchors.append(anchor)

    def _new_hotkey_threaded(self, anchor:ANAnchor, hotkey_type:str, callback:callable):
        config_model = self._engine().get_config_model()
        hotkey_state = config_model.get_global_hotkey_state()
        config_model.set_global_hotkey_state(False)

        new_hotkey = self._engine().get_keyboard_controller().record_hotkey()
        anchor.set_hotkey(hotkey_type, new_hotkey)

        config_model.set_global_hotkey_state(hotkey_state)
        self._engine().update()
        callback()

    def _bind_click(self, anchor:ANAnchor):
        def action():
            if self._engine().get_config_model().get_global_hotkey_state():
                mouse_controller = self._engine().get_mouse_controller()
                mouse_controller.set_position(anchor.get_position())
                mouse_controller.click(anchor.get_action())

        self._engine().get_keyboard_controller().set_hotkey(anchor.get_hotkey('click'), action)

    def _bind_record(self, anchor:ANAnchor):
        def action():
            if self._engine().get_config_model().get_global_hotkey_state():
                mouse_controller = self._engine().get_mouse_controller()
                anchor.set_anchor_position(mouse_controller.get_position())
                self._engine().update()
        
        self._engine().get_keyboard_controller().set_hotkey(anchor.get_hotkey('record'), action)