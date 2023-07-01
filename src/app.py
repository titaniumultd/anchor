import json
import os
import tkinter as tk

from pynput.mouse import Controller as MouseController

from src.anchor import Anchor

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

        self.mouse = MouseController()

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
        new_anchor = Anchor(self.root, len(self.anchors), self.mouse)
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

    def load_state(self) -> bool:
        if os.path.exists('config/state.json'):
            with open('config/state.json', 'r') as file:
                state = json.load(file)

            for anchor_state in state:
                new_anchor = Anchor(self.root, len(self.anchors), self.mouse)
                new_anchor.record_hotkey.hotkey.set(anchor_state['record_hotkey'])
                new_anchor.click_hotkey.hotkey.set(anchor_state['click_hotkey'])
                if anchor_state['mouse_position']:
                    new_anchor.mouse_position = anchor_state['mouse_position']
                new_anchor.action_combobox.set(anchor_state['action'])
                new_anchor.remove_anchor_button['command'] = lambda anchor=new_anchor: self.remove_anchor(anchor)
                new_anchor.grid_ui_elements()
                self.anchors.append(new_anchor)
            return True
        return False
            
    def save_state(self):
        state = [{
            'record_hotkey': anchor.record_hotkey.hotkey.get(),
            'click_hotkey': anchor.click_hotkey.hotkey.get(),
            'mouse_position': anchor.mouse_position if hasattr(anchor, 'mouse_position') else None,
            'action': anchor.action_combobox.get(),
        } for anchor in self.anchors]

        with open('config/state.json', 'w') as file:
            json.dump(state, file)