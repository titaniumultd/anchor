
import tkinter as tk

from src.ui.custom.frame import ANFrame
from src.ui.anchor.anchor_list import ANAnchorList

class ANAnchorSettings(ANFrame):
    """
    Top level anchor settings view container. Should contain a list of anchors, editable by the user.
    """

    def load_subviews(self):
        self.anchor_list = ANAnchorList(self, self.get_engine())
        self.anchor_list.pack(expand = True, fill = 'both')

        self.activate_hotkeys_button = tk.Button(self, text = "Activate hotkeys", command = self.activate_hotkeys)
        self.activate_hotkeys_button.pack(side = 'right', anchor = tk.S, pady = (10, 0))

    def activate_hotkeys(self):
        self._engine().get_anchors_controller().activate_hotkeys()

        