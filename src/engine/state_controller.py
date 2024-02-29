
import json
import weakref

from pathlib import Path

from src.common.interfaces.controllers.state_controller_interface import ANStateControllerInterface
from src.common.interfaces.engine_interface import ANEngineInterface


class ANStateController(ANStateControllerInterface, object):
    """
    Manages the saved state.
    """
    def __init__(self, engine: ANEngineInterface):

        self._engine = weakref.ref(engine)

        self._state:dict = {}

        self.state_file_path = Path('config/state.json')
        self._load_state()

    # Public Methods

    def get_state(self) -> dict:
        return self._state
    
    def update_state(self):
        anchors = self._engine().get_anchor_controller().get_anchors()
        state = {}
        for i, anchor in enumerate(anchors):
            state[f'anchor {i}'] = {
                'record_hotkey': anchor.get_hotkey('record'),
                'click_hotkey': anchor.get_hotkey('click'),
                'mouse_position': anchor.get_position(),
                'action': anchor.get_action()
            }
        self._state = state
        self._write_state_file()

    # Private Methods
            
    def _load_state(self):
        if self._state_file_exists():
            self._state = self._read_state_file()
        else:
            self._create_state_file()

    def _state_file_exists(self) -> bool:
        if self.state_file_path.exists():
            return True
        else:
            return False
    
    def _create_state_file(self):
        self.state_file_path.parent.mkdir(parents=True, exist_ok=True)
        with self.state_file_path.open('w') as file:
            json.dump(self._state, file, default=str)

    def _read_state_file(self):
        with self.state_file_path.open('r') as file:
            return json.load(file)
        
    def _write_state_file(self):
        with self.state_file_path.open('w') as file:
            json.dump(self._state, file, default=str)