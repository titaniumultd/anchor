import tkinter as tk
from tkinter import ttk

from pynput.mouse import Button as MouseButton

from src.hotkey import HotKey


class Anchor:
    def __init__(self, root, index, mouse, notifier):
        '''
        Instanced class to hold sets of hotkeys and ui components
        '''
        self.root = root
        self.index = index
        self.mouse = mouse
        self.anchor_frame = tk.Frame(self.root)
        self.anchor_frame.grid()
        self.notifier = notifier

        # initialize UI elements
        self.record_position_label = tk.Label(self.anchor_frame)
        self.record_position_entry = tk.Entry(self.anchor_frame)
        self.record_position_button = tk.Button(self.anchor_frame, text="Set", command=lambda: self.record_hotkey.start_capturing())

        self.click_position_label = tk.Label(self.anchor_frame)
        self.click_position_entry = tk.Entry(self.anchor_frame)
        self.click_position_button = tk.Button(self.anchor_frame, text="Set", command=lambda: self.click_hotkey.start_capturing())

        self.action_label = tk.Label(self.anchor_frame)
        self.action_combobox = ttk.Combobox(self.anchor_frame, values=["left click", "right click", "double left click"])
        self.remove_anchor_button = tk.Button(self.anchor_frame, text="Delete")

        self.separator = tk.Label(self.anchor_frame, text="")

        # group all the elements in the frame
        self.ui_elements = [
            self.record_position_label, self.record_position_entry, self.record_position_button,
            self.click_position_label, self.click_position_entry, self.click_position_button,
            self.action_label, self.action_combobox, self.remove_anchor_button, self.separator
        ]

        # initialize hotkeys
        self.record_hotkey = HotKey(self.record_position_entry, self.record_position)
        self.click_hotkey = HotKey(self.click_position_entry, self.click_position)
        self.record_hotkey.hotkey.set(f'ctrl+alt+{index+1}')
        self.click_hotkey.hotkey.set(f'alt+{index+1}')
        self.record_hotkey.activate()
        self.click_hotkey.activate()

        self.action_combobox.current(0)


    def grid_ui_elements(self):
        '''
        Called after creation to align ui components
        '''
        self.record_position_label.config(text=f"Drop Anchor {self.index+1}:")
        self.record_position_label.grid(row=self.index*5, column=0, pady=2)
        self.record_position_entry.grid(row=self.index*5, column=1)
        self.record_position_button.grid(row=self.index*5, column=2)

        self.click_position_label.config(text=f"Hotkey {self.index+1}:")
        self.click_position_label.grid(row=self.index*5+1, column=0, pady=2)
        self.click_position_entry.grid(row=self.index*5+1, column=1)
        self.click_position_button.grid(row=self.index*5+1, column=2)

        self.action_label.config(text=f"Action {self.index+1}:")
        self.action_label.grid(row=self.index*5+2, column=0, pady=2)
        self.action_combobox.grid(row=self.index*5+2, column=1)

        self.remove_anchor_button.grid(row=self.index*5+2, column=2, padx=3)

        self.separator.grid(row=self.index*5+3, column=0, pady=2)  # Add vertical padding between anchors

    def record_position(self):
        self.mouse_position = self.mouse.position
        self.notifier.notify()

    def click_position(self):
        if self.mouse_position:
            self.mouse.position = self.mouse_position
            action = self.action_combobox.get()
            if action == "left click":
                self.mouse.click(MouseButton.left)
            elif action == "right click":
                self.mouse.click(MouseButton.right)
            elif action == "double left click":
                self.mouse.click(MouseButton.left, 2)

    def destroy(self):
        self.record_hotkey.deactivate()
        self.click_hotkey.deactivate()

        self.anchor_frame.destroy()
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
    def from_dict(dictionary, root, mouse, notifier):
        '''
        Creates a new anchor instance from a dictionary.
        '''
        new_anchor = Anchor(root, dictionary['index'], mouse, notifier)
        new_anchor.record_hotkey.hotkey.set(dictionary['record_hotkey'])
        new_anchor.click_hotkey.hotkey.set(dictionary['click_hotkey'])
        new_anchor.mouse_position = dictionary['mouse_position']
        new_anchor.action_combobox.set(dictionary['action'])
        return new_anchor