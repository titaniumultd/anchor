
import keyboard as kb


class ANKeyboardController(object):

    def record_hotkey(self) -> str:
        kb.stash_state()
        return kb.read_hotkey()
    
    def set_hotkey(self, hotkey:str, action:callable):
        if hotkey == 'undefined':
            return
        self.clear_hotkey(hotkey)
        kb.add_hotkey(hotkey, action)

    def clear_hotkey(self, hotkey:str):
        if hotkey == 'undefined':
            return
        try:
            kb.remove_hotkey(hotkey)
        except:
            pass