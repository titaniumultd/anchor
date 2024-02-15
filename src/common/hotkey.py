
import keyboard
import logging
import threading

from src.common.interfaces.view_model_interface import ANViewModelInterface

logging.basicConfig(filename='error.log', level=logging.INFO)


class ANHotKey(object):
    """
    Class to hold the individual hotkeys and provide services to set and activate the hotkeys.
    """
    def __init__(self, action: callable, view_model: ANViewModelInterface):
        self.action = action
        self.hotkey = ''
        self.view_model = view_model

    def activate(self) -> None:
        """
        Activate the registered hotkey.
        """
        if self.hotkey != None and len(self.hotkey) > 0:
            try:
                keyboard.add_hotkey(self.hotkey, self.action)
            except ValueError as err:
                logging.error(f"Error activating hotkey: {err}")

    def deactivate(self) -> None:
        """
        Deactivate the registered hotkey.
        """
        try:
            keyboard.remove_hotkey(self.hotkey)
        except KeyError:
            pass
    
    def set_new_hotkey(self, callback: callable):
        threading.Thread(target=self._set_new_hotkey, args=[callback], daemon=True).start()

    def _set_new_hotkey(self, callback: callable) -> None:
        """
        Sets a new hotkey combination. Calls a callback on completion
        """
        self.deactivate()
        keyboard.stash_state() # fixes key retention after reading issue
        hotkey = keyboard.read_hotkey()
        self.hotkey = hotkey
        self.activate()
        self.view_model.restore_ui()