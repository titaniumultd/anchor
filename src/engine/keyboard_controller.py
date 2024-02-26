
import keyboard as kb


class ANKeyboardController(object):
    def __init__(self):
        pass

    def record_hotkey(self) -> str:
        return kb.read_hotkey()