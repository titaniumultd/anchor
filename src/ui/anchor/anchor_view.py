
import customtkinter as ctk

from src.common.interfaces.ui.anchor_view_model_interface import ANAnchorViewModelInterface
from src.ui.custom.frame import ANFrame
from src.common.variables import ACTIONS

X_PADDING = 4
Y_PADDING = 4

class ANAnchorView(ANFrame):

    def __init__(self, 
                 root: ctk.CTk,
                 view_model: ANAnchorViewModelInterface
                 ):
        super().__init__(root)
        
        self._root = root
        self._view_model = view_model

        self._record_hotkey_combo: ctk.StringVar = self._view_model.record_hotkey_strvar
        self._click_hotkey_combo: ctk.StringVar = self._view_model.click_hotkey_strvar
        self._anchor_action: str = self._view_model.anchor_action

        self.grid(column=0, sticky='news', pady=10)

    def load_subviews(self):
        self._init_subviews()
        self._layout_subviews()
        self._set_subview_content()

    def _init_subviews(self):
        self.columnconfigure((0, 1, 2), weight=1)
        self.rowconfigure((0, 1, 2), weight=1)

        self.record_position_label = ctk.CTkLabel(self)
        self.record_position_entry = ctk.CTkEntry(self)
        self.record_position_button = ctk.CTkButton(self, text="Record", command=self._update_record_hotkey)

        self.click_position_label = ctk.CTkLabel(self)
        self.click_position_entry = ctk.CTkEntry(self)
        self.click_position_button = ctk.CTkButton(self, text="Record", command=self._update_click_hotkey)

        self.action_label = ctk.CTkLabel(self)
        self.action_combobox = ctk.CTkComboBox(self, values=ACTIONS, command=self._update_action)

    def _layout_subviews(self):
        self.record_position_label.grid(row=0, column=0, pady=Y_PADDING, sticky='e')
        self.record_position_entry.grid(row=0, column=1, padx=X_PADDING, pady=Y_PADDING, sticky='news')
        self.record_position_button.grid(row=0, column=2, sticky='w')

        self.click_position_label.grid(row=1, column=0, pady=Y_PADDING, sticky='e')
        self.click_position_entry.grid(row=1, column=1, padx=X_PADDING, pady=Y_PADDING, sticky='news')
        self.click_position_button.grid(row=1, column=2, sticky='w')

        self.action_label.grid(row=2, column=0, pady=Y_PADDING, sticky='e')
        self.action_combobox.grid(row=2, column=1, padx=X_PADDING, pady=Y_PADDING, sticky='news')
    
    def _set_subview_content(self):
        self.record_position_label.configure(text = f"Drop Anchor:")
        self.record_position_entry.configure(textvariable = self._record_hotkey_combo)

        self.click_position_label.configure(text=f"Action Hotkey:")
        self.click_position_entry.configure(textvariable = self._click_hotkey_combo)

        self.action_label.configure(text=f"Action:")
        self.action_combobox.set(self._anchor_action)
    
    def _update_record_hotkey(self):
        self._view_model.request_hotkey_update('record')
    
    def _update_click_hotkey(self):
        self._view_model.request_hotkey_update('click')

    def _update_action(self):
        self._view_model.update_action(self.action_combobox.get())