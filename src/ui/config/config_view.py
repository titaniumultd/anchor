
import customtkinter as ctk

from src.ui.custom.frame import ANFrame
from src.common.interfaces.ui.config_view_model_interface import ANConfigViewModelInterface
from src.ui.anchor.anchor_list import ANAnchorList


class ANConfigView(ANFrame, object):
    def __init__(self, root: ctk.CTk, view_model: ANConfigViewModelInterface):
        self._root = root
        self._view_model = view_model

        self._global_hotkeys_enabled:bool = True
        
        self.grid_columnconfigure(0, weight=1)

        super().__init__(self._root)

    def update(self, update_packet: dict):
        self._global_hotkeys_enabled = update_packet['hotkey_state']

    def load_subviews(self):
        self._load_anchor_subview()
        self._load_config_subview()

    def _load_anchor_subview(self):
        self._anchor_list = ANAnchorList(self._root, self._view_model.get_anchor_view_model())
    
    def _load_config_subview(self):
        self.activate_hotkeys_button = ctk.CTkCheckBox(self, text="Activate hotkeys", command=self._toggle_global_hotkeys)
        self.activate_hotkeys_button.pack(side='right', anchor=ctk.S, pady=(10, 0))

    def _toggle_global_hotkeys(self):
        self._view_model.toggle_global_hotkeys()