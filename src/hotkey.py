import keyboard
import tkinter

class HotKey:
    def __init__(self, entry_field, action):
        self.entry_field = entry_field
        self.action = action
        self.hotkey = tkinter.StringVar() # Store the hotkey value in a StringVar
        self.entry_field.config(textvariable=self.hotkey) # Set the textvariable of the Entry field

    def start_capturing(self):
        self.captured_keys = []
        keyboard.hook_key('esc', self.stop_capturing, suppress=True)
        keyboard.on_press(self.on_key_press, suppress=True)
        keyboard.on_release(self.on_key_release, suppress=True)

    def stop_capturing(self, e):
        keyboard.unhook_all()
        self.hotkey.set('+'.join(self.captured_keys)) # Set the Entry field's value using the StringVar
        self.captured_keys = []

    def on_key_press(self, e):
        self.captured_keys.append(e.name)
        return False  # allow key events to pass to other handlers

    def on_key_release(self, e):
        if self.is_capturing:
            self.hotkey = '+'.join(self.captured_keys)
            self.stop_capturing()
        return False 

    def set_action(self, action):
        self.action = action

    def set_hotkey(self, hotkey):
        self.hotkey = hotkey

    def activate(self):
        # This will activate the hotkey and bind the action to it.
        keyboard.add_hotkey(self.hotkey, self.action)

    def deactivate(self):
        # This will deactivate the hotkey
        try:
            keyboard.remove_hotkey(self.hotkey)
        except KeyError:
            pass