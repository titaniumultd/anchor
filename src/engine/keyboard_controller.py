
import keyboard as kb


class ANKeyboardController(object):

    def record_hotkey(self) -> str:
        hotkey = kb.read_hotkey()
        kb.stash_state() # retains keys after reading unless you have double stash calls :shrug:
        kb.stash_state()
        return hotkey
    
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