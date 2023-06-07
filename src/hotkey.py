import keyboard
import tkinter

class HotKey:
    def __init__(self, entry_field, action):
        self.entry_field = entry_field
        self.action = action
        self.hotkey = tkinter.StringVar(value='')
        self.entry_field.config(textvariable=self.hotkey) # Set the textvariable of the Entry field
        self.is_capturing = False

    def start_capturing(self):
        print("Starting capture")
        self.is_capturing = True
        self.captured_keys = []
        keyboard.hook_key('esc', self.stop_capturing, suppress=True)
        keyboard.on_press(self.on_key_press, suppress=True)
        keyboard.on_release(self.on_key_release, suppress=True)

    def stop_capturing(self, e=None):
        keyboard.unhook_all()
        self.is_capturing = False
        return False

    def on_key_press(self, e):
        print(f"Key pressed: {e.name}")
        self.captured_keys.append(e.name)
        return False

    def on_key_release(self, e):
        if self.is_capturing:
            self.stop_capturing()
            self.hotkey.set('+'.join(self.captured_keys))  # Changed from .value to .set()
            self.captured_keys = []
        return False 

    def activate(self):
        if self.hotkey.get():
            keyboard.add_hotkey(self.hotkey.get(), self.action)

    def deactivate(self):
        try:
            keyboard.remove_hotkey(self.hotkey.get())  # Changed from .hotkey to .hotkey.get()
        except KeyError:
            pass