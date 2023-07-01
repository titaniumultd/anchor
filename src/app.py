import json
import os
import tkinter as tk

from pynput.mouse import Controller as MouseController

from src.anchor import Anchor
from src.notifier import Notifier

MAX_ANCHORS = 5


class Singleton:
    _instance = None
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance
    

class App(Singleton):
    '''
    Our main app class, includes runtime loop and some dedicated ui components
    '''

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Anchor")
        self.root.grid_columnconfigure(0, weight=1)  # adjust size with window
        self.root.grid_columnconfigure(1, weight=1)
        self.root.grid_rowconfigure(0, weight=1)

        self.notifier = Notifier()
        self.notifier.register_listener(self)

        self.mouse = MouseController()

        self.state_file_path = 'config/state.json'
        self.current_profile = 'default'

        self.anchors = []

        self.add_anchor_button = tk.Button(self.root, text="New Anchor", command=self.drop_an_anchor)
        self.activate_hotkeys_button = tk.Button(self.root, text="Activate hotkeys", command=self.activate_hotkeys)        

    def run(self):
        self.add_anchor_button.grid(row=0, column=0, sticky='w', padx=5)
        self.activate_hotkeys_button.grid(row=0, column=0, sticky='e', padx=5)
        if self.load_state():
            self.activate_hotkeys()
        if len(self.anchors) == 0:
            self.drop_an_anchor()
        
        self.root.mainloop()

    def drop_an_anchor(self):
        '''
        colloquial for creating a new anchor
        '''
        if len(self.anchors) >= MAX_ANCHORS:
            return
        new_anchor = Anchor(self.root, len(self.anchors), self.mouse, self.notifier)
        new_anchor.remove_anchor_button['command'] = lambda: self.remove_anchor(new_anchor)
        new_anchor.grid_ui_elements()
        self.anchors.append(new_anchor)

        self.save_state()

    def remove_anchor(self, anchor):
        index = self.anchors.index(anchor)
        self.anchors.remove(anchor)
        anchor.destroy()

        # Shift down the remaining anchors
        for i in range(index, len(self.anchors)):
            self.anchors[i].index = i
            self.anchors[i].grid_ui_elements()

        self.save_state()

    def activate_hotkeys(self):
        for anchor in self.anchors:
            anchor.record_hotkey.activate()
            anchor.click_hotkey.activate()

    def load_state(self):
        if not os.path.exists(self.state_file_path):
            os.makedirs(os.path.dirname(self.state_file_path), exist_ok=True)
            state = {
                'last_profile': 'default',
                'profiles': {'default': []}
            }
            with open(self.state_file_path, 'w') as file:
                json.dump(state, file, default=str)
            return state
        else:
            with open(self.state_file_path, 'r') as file:
                state = json.load(file)
                if isinstance(state, dict) and 'profiles' in state and isinstance(state['profiles'], dict):
                    self.current_profile = state['last_profile']
                    profiles = state['profiles']
                    if self.current_profile in profiles:
                        anchors = profiles[self.current_profile]
                        for anchor_dict in anchors:
                            new_anchor = Anchor.from_dict(anchor_dict, self.root, self.mouse, self.notifier)
                            new_anchor.grid_ui_elements()
                            self.anchors.append(new_anchor)
                else:
                    print(f"Invalid state.json format. Expected a dictionary with 'profiles' key.")
                    return {
                        'last_profile': 'default',
                        'profiles': {'default': []}
                    }

    def save_state(self):
        state = [anchor.to_dict() for anchor in self.anchors]
        with open(self.state_file_path, 'r+') as file:
            current_state = json.load(file)
            if isinstance(current_state, dict) and 'profiles' in current_state and isinstance(current_state['profiles'], dict):
                profiles = current_state['profiles']
                profiles[self.current_profile] = state
                current_state['last_profile'] = self.current_profile
                file.seek(0)
                file.truncate()
                json.dump(current_state, file, default=str)
            else:
                print(f"Invalid state.json format in save_state. Expected a dictionary with 'profiles' key.")

    def update(self):
        self.save_state()