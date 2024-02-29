

class ANConfigModel(object):
    def __init__(self):
        self._global_hotkey_state:bool = True

    def toggle_global_hotkey_state(self) -> bool:
        self._global_hotkey_state = not self._global_hotkey_state
        return self._global_hotkey_state
    
    def get_global_hotkey_state(self) -> bool:
        return self._global_hotkey_state