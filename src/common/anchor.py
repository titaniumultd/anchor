import tkinter as tk
from tkinter import ttk

from pynput.mouse import Button as MouseButton

from src.hotkey import HotKey


class ANAnchor:

    ACTIONS = ["left click", "right click"]
    ACTION_BUTTON_CLICKS = {
        "left click": (MouseButton.left, 1),
        "right click": (MouseButton.right, 1)
    }

    def __init__(self, root, index, mouse, notifier):
        '''
        Instanced class to hold sets of hotkeys and ui components
        '''
        self.root = root
        self.index = index
        self.mouse = mouse
        self.anchor_frame = tk.Frame(self.root)
        self.anchor_frame.grid(columnspan=3) #This forces the newly added Anchors to span the 3 columns in the original grid
        self.notifier = notifier
        self.mouse_position = None

        self._init_ui()
        self._init_hotkeys()

        self.action_combobox.current(0)

    def _init_ui(self):
        '''Initialize UI elements and configure grid layout.'''
        self.record_position_label = tk.Label(self.anchor_frame)
        self.record_position_entry = tk.Entry(self.anchor_frame)
        self.record_position_button = tk.Button(self.anchor_frame, text="Set")

        self.click_position_label = tk.Label(self.anchor_frame)
        self.click_position_entry = tk.Entry(self.anchor_frame)
        self.click_position_button = tk.Button(self.anchor_frame, text="Set")

        self.action_label = tk.Label(self.anchor_frame)
        self.action_combobox = ttk.Combobox(self.anchor_frame, values=ANAnchor.ACTIONS)

        self.separator = tk.Label(self.anchor_frame, text="")
        

        # group all the elements in the frame
        self.ui_elements = [
            self.record_position_label, self.record_position_entry, self.record_position_button,
            self.click_position_label, self.click_position_entry, self.click_position_button,
            self.action_label, self.action_combobox, self.separator
        ]

        # Set the grid layout
        self._grid_ui_elements()

    def _grid_ui_elements(self):
        '''
        Called after creation to align ui components
        '''
        self.record_position_label.config(text=f"Drop Anchor {self.index+1}:", justify="right")
        self.record_position_label.grid(row=self.index*5, column=0, padx=8, pady=2, sticky="e")
        self.record_position_entry.grid(row=self.index*5, column=1, sticky="ew")
        self.record_position_button.grid(row=self.index*5, column=2, padx=8, sticky="ew")

        self.click_position_label.config(text=f"Hotkey {self.index+1}:", justify="right")
        self.click_position_label.grid(row=self.index*5+1, column=0, padx=8, pady=2, sticky="e")
        self.click_position_entry.grid(row=self.index*5+1, column=1, sticky="ew")
        self.click_position_button.grid(row=self.index*5+1, column=2, padx=8, sticky="ew")

        self.action_label.config(text=f"Action {self.index+1}:", justify="right")
        self.action_label.grid(row=self.index*5+2, column=0, padx=8, pady=2, sticky="e")
        self.action_combobox.grid(row=self.index*5+2, column=1, sticky="ew")

        self.separator.grid(row=self.index*5+3, column=0, pady=7)  # Add vertical padding between anchors

    def _init_hotkeys(self):
        '''Initialize hotkeys and bind them to their corresponding functions.'''
        self.record_hotkey = HotKey(self.record_position_entry, self._record_position)
        self.click_hotkey = HotKey(self.click_position_entry, self._click_position)
        self.record_hotkey.hotkey.set(f'ctrl+alt+{self.index+1}')
        self.click_hotkey.hotkey.set(f'alt+{self.index+1}')
        self.record_hotkey.activate()
        self.click_hotkey.activate()

    def _record_position(self):
        self.mouse_position = self.mouse.position
        self.notifier.notify()

    def _click_position(self):
        '''Perform the configured action at the recorded mouse position.'''
        if self.mouse_position:
            self.mouse.position = self.mouse_position
            action = self.action_combobox.get()
            button, clicks = ANAnchor.ACTION_BUTTON_CLICKS.get(action, (MouseButton.left, 1))
            self.mouse.click(button, clicks)

    def destroy(self, save=True):
        self.record_hotkey.deactivate()
        self.click_hotkey.deactivate()

        self.anchor_frame.destroy()
        if save:
            self.notifier.notify()
    
    def to_dict(self):
        '''
        Converts the anchor instance to a dictionary for serialization.
        '''
        return {
            'index': self.index,
            'record_hotkey': self.record_hotkey.hotkey.get(),
            'click_hotkey': self.click_hotkey.hotkey.get(),
            'mouse_position': self.mouse_position if hasattr(self, 'mouse_position') else None,
            'action': self.action_combobox.get()
        }

    @staticmethod
    def from_dict(anchor_dict, root, mouse, notifier, remove_callback=None):
        new_anchor = ANAnchor(root, anchor_dict['index'], mouse, notifier)
        new_anchor.record_hotkey.hotkey.set(anchor_dict['record_hotkey'])
        new_anchor.click_hotkey.hotkey.set(anchor_dict['click_hotkey'])
        if anchor_dict['mouse_position']:
            new_anchor.mouse_position = anchor_dict['mouse_position']
        else:
            new_anchor.mouse_position = None
        new_anchor.action_combobox.set(anchor_dict['action'])

        return new_anchor