import tkinter as tk
from tkinter import ttk
from hotkey import HotKey
from pynput.mouse import Button as MouseButton, Controller as MouseController


class Anchor:
    def __init__(self, root, index, mouse):
        self.root = root
        self.index = index
        self.mouse = mouse

        # initialize UI elements
        self.record_position_label = tk.Label(root)
        self.record_position_entry = tk.Entry(root)
        self.record_position_button = tk.Button(root, text="Set", command=lambda: self.record_hotkey.start_capturing())

        self.click_position_label = tk.Label(root)
        self.click_position_entry = tk.Entry(root)
        self.click_position_button = tk.Button(root, text="Set", command=lambda: self.click_hotkey.start_capturing())

        self.action_label = tk.Label(root)
        self.action_combobox = ttk.Combobox(root, values=["left click", "right click", "double left click"])
        self.remove_anchor_button = tk.Button(root, text="Delete")

        self.ui_elements = [
            self.record_position_label, self.record_position_entry, self.record_position_button,
            self.click_position_label, self.click_position_entry, self.click_position_button,
            self.action_label, self.action_combobox, self.remove_anchor_button
        ]

        # initialize hotkeys
        self.record_hotkey = HotKey(self.record_position_entry, self.record_position)
        self.click_hotkey = HotKey(self.click_position_entry, self.click_position)
        self.record_hotkey.hotkey.set(f'ctrl+alt+{index+1}') # Set the default hotkey values using the StringVar
        self.click_hotkey.hotkey.set(f'alt+{index+1}')

        self.action_combobox.current(0)

    def create_ui_elements(self):
        self.record_position_label = tk.Label(self.root, text=f"Drop Anchor {self.index+1}:")
        self.record_position_button = tk.Button(self.root, text="Set", command=self.record_hotkey.start_capturing)
        
        self.click_position_label = tk.Label(self.root, text=f"Hotkey {self.index+1}:")
        self.click_position_button = tk.Button(self.root, text="Set", command=self.click_hotkey.start_capturing)
        
        self.action_label = tk.Label(self.root, text=f"Action {self.index+1}:")
        self.action_combobox = ttk.Combobox(self.root, values=["left click", "right click", "double left click"])
        self.action_combobox.current(0)

        self.remove_anchor_button = tk.Button(self.root, text="Delete")

    def grid_ui_elements(self):
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

        separator = tk.Label(self.root, text="")
        separator.grid(row=self.index*5+3, column=0, pady=2)  # Add vertical padding between anchors

    def record_position(self):
        self.mouse_position = self.mouse.position

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
        # Remove hotkeys
        self.record_hotkey.deactivate()
        self.click_hotkey.deactivate()
        
        # Destroy UI elements
        self.record_position_label.destroy()
        self.record_position_button.destroy()
        self.click_position_label.destroy()
        self.click_position_button.destroy()
        self.action_label.destroy()
        self.action_combobox.destroy()
        self.remove_anchor_button.destroy()
