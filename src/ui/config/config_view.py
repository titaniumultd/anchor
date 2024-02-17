
from customtkinter import CTk

from src.ui.custom.frame import ANFrame
from src.common.interfaces.anchor_view_interface import ANAnchorViewInterface
from src.ui.anchor.anchor_view import ANAnchorView


class ANConfigView(ANFrame):
    def __init__(self, root: CTk, view_model: ANAnchorViewInterface):

        self._root = root
        self._view_model = view_model

        self._global_hotkeys_enabled:bool = True

        super().__init__(self._root)

    def load_subviews(self):
        anchors = self._view_model.get_anchors()
                
        for anchor in anchors:
            anchor_view:ANAnchorViewInterface = ANAnchorView(self._root, anchor)
            anchor_view.grid(column=0, sticky='news', pady=10)

    def update(self, update_packet: dict):
        self._global_hotkeys_enabled = update_packet['hotkey_state']

    def _toggle_global_hotkeys(self):
        self._



'''import customtkinter as ctk

from src.ui.custom.frame import ANFrame
from src.ui.anchor.anchor_list import ANAnchorList

class ANAnchorSettings(ANFrame):
    """
    Top level anchor settings view container. Should contain a list of anchors, editable by the user.
    """

    def load_subviews(self):
        self.anchor_list = ANAnchorList(self.get_root(), self.get_view())
        self.anchor_list.pack(expand=True, fill='both')

        self.activate_hotkeys_button = ctk.CTkCheckBox(self, text="Activate hotkeys", command=self._toggle_hotkeys)
        self.activate_hotkeys_button.pack(side='right', anchor=ctk.S, pady=(10, 0))
        self.activate_hotkeys_button.select()

    def _toggle_hotkeys(self):
        self._view().toggle_hotkeys()'''