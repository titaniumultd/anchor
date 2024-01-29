
import json

from pathlib import Path

from src.common.interfaces.state_interface import ANStateControllerInterface

class ANStateController(ANStateControllerInterface, object):
    """
    Manages the application state.
    """
    def __init__(self):
        self._state = None

        self.state_file_path = Path('config/state.json')
        self._ensure_state_file_exists()

    # Public Methods

    def load_state(self) -> None:
        self._state = self._read_state_file()

    def save_state(self) -> None:
        if self._state != None:
            self._write_state_file(self._state)

        # old implementation
        # self._state = self._read_state_file()

        # if 'profiles' in state:
        #     state['profiles'][self.current_profile] = [anchor.to_dict() for anchor in self.anchors]
        #     state['last_profile'] = self.current_profile
        #     self._write_state_file(state)
        # else:
        #     logging.error("Invalid state.json format in save_state. Expected a dictionary with 'profiles' key.")

    def get_state(self) -> dict:
        return self._state

    # Private Methods

    def _ensure_state_file_exists(self) -> None:
        if not self.state_file_path.exists():
            self.state_file_path.parent.mkdir(parents=True, exist_ok=True)
            self._state = {
                'last_profile': 'default',
                'profiles': {'default': []}
            }
            with self.state_file_path.open('w') as file:
                json.dump(self._state, file, default=str)
    
    def _read_state_file(self):
        with self.state_file_path.open('r') as file:
            return json.load(file)
        
    def _write_state_file(self, state):
        with self.state_file_path.open('w') as file:
            json.dump(state, file, default=str)
    