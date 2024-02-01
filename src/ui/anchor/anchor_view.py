
import tkinter as tk
from tkinter import ttk

from src.common.anchor import ANAnchor
from src.ui.custom.frame import ANFrame

X_PADDING = 4
Y_PADDING = 4


class ANAnchorView(ANFrame):
    """
    View contaiing anchor details and buttons.
    """

    def __init__(self, 
                 master, 
                 engine, 
                 anchor):
        self._anchor = anchor

        super().__init__(master, engine)

    def load_subviews(self):
        self.columnconfigure((0, 1, 2), weight = 1)
        self.rowconfigure((0, 1, 2), weight = 1)

        self.record_position_label = tk.Label(self)
        self.record_position_entry = tk.Entry(self)
        self.record_position_button = tk.Button(self, text="Set", command=self._update_record_hotkey)

        self.click_position_label = tk.Label(self)
        self.click_position_entry = tk.Entry(self)
        self.click_position_button = tk.Button(self, text="Set", command=self._update_click_hotkey)

        self.action_label = tk.Label(self)
        self.action_combobox = ttk.Combobox(self, values=ANAnchor.ACTIONS)

        # Layout

        self.record_position_label.config(text=f"Drop Anchor {self.index + 1}:")
        self.record_position_label.grid(row = 0, column = 0, pady = Y_PADDING, sticky = 'e')
        self.record_position_entry.grid(row = 0, column = 1, padx = X_PADDING, pady = Y_PADDING, sticky = 'news')
        self.record_position_button.grid(row = 0, column = 2, sticky = 'w')

        self.click_position_label.config(text=f"Hotkey {self.index + 1}:")
        self.click_position_label.grid(row = 1, column = 0, pady = Y_PADDING, sticky = 'e')
        self.click_position_entry.grid(row = 1, column = 1, padx = X_PADDING, pady = Y_PADDING, sticky = 'news')
        self.click_position_button.grid(row = 1, column = 2, sticky = 'w')

        self.action_label.config(text=f"Action {self.index + 1}:")
        self.action_label.grid(row = 2, column = 0, pady = Y_PADDING, sticky = 'e')
        self.action_combobox.grid(row = 2, column = 1, padx = X_PADDING, pady = Y_PADDING, sticky = 'news')

        self.action_combobox.current(0)

    @property
    def index(self):
        return self._anchor.index

    def _update_record_hotkey(self):
        pass

    def _update_click_hotkey(self):
        pass