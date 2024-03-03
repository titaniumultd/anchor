
import keyboard as kb


class ANKeyboardController(object):

    def record_hotkey(self) -> str:
        kb.stash_state()
        return kb.read_hotkey()
    
    def set_hotkey(self, hotkey:str, action:callable):
        try:
            kb.remove_hotkey(hotkey)
        except:
            pass

        kb.add_hotkey(hotkey, action)

    def clear_hotkey(self, hotkey:str):
        try:
            kb.remove_hotkey(hotkey)
        except:
            print(f'Failed to remove keybind:{hotkey}')