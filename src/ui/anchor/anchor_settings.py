
import customtkinter as ctk

from src.ui.custom.frame import ANFrame
from src.ui.anchor.anchor_list import ANAnchorList

class ANAnchorSettings(ANFrame):
    """
    Top level anchor settings view container. Should contain a list of anchors, editable by the user.
    """

    def load_subviews(self):
        self.anchor_list = ANAnchorList(self, self.get_engine())
        self.anchor_list.pack(expand=True, fill='both')

        self.hotkeys_enabled = ctk.IntVar()
        self.activate_hotkeys_button = ctk.CTkCheckBox(self, text="Activate hotkeys", command=self.activate_hotkeys, variable=self.hotkeys_enabled)
        self.activate_hotkeys_button.pack(side='right', anchor=ctk.S, pady=(10, 0))

    def activate_hotkeys(self):
        if self.hotkeys_enabled.get() == 1:
            self._engine().get_anchors_controller().activate_hotkeys()
        else:
            self._engine().get_anchors_controller().deactivate_hotkeys()

        