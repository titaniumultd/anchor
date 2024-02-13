
import keyboard
import logging

logging.basicConfig(filename='error.log', level=logging.INFO)


class ANHotKey:
    """
    Class to hold the individual hotkeys and provide services to set and activate the hotkeys.
    """
    def __init__(self, action: callable):
        self.action = action
        self.hotkey = ''
    #    self.is_capturing = False

    '''    def start_capturing(self) -> None:
        """
        Start capturing keystrokes for hotkey registration.
        """
        logging.info("Starting capture")
        self.is_capturing = True
        self.captured_keys = []
        keyboard.hook_key('esc', self.stop_capturing, suppress=True)
        keyboard.on_press(self.on_key_press, suppress=True)
        keyboard.on_release(self.on_key_release, suppress=True)

    def stop_capturing(self, e=None) -> bool:
        """
        Stop capturing keystrokes for hotkey registration.
        """
        keyboard.unhook_all()
        self.is_capturing = False
        return False

    def on_key_press(self, e: keyboard.KeyboardEvent) -> bool:
        """
        Handle a key press event during hotkey registration.
        """
        logging.info(f"Key pressed: {e.name}")
        self.captured_keys.append(e.name)
        return False

    def on_key_release(self, e: keyboard.KeyboardEvent) -> bool:
        """
        Handle a key release event during hotkey registration.
        """
        if self.is_capturing:
            self.stop_capturing()
            self.hotkey = '+'.join(self.captured_keys)
            self.captured_keys = []
        return False 
    '''

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

    def set_new_hotkey(self) -> None:
        """
        Sets a new hotkey combination.
        """
        self.deactivate()
        hotkey = keyboard.read_hotkey()
        self.hotkey = hotkey
        self.activate()