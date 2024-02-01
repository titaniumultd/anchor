
import weakref
import tkinter as tk

from src.common.interfaces.engine_interface import ANEngineInterface
from src.ui.anchor_settings import ANAnchorSettings

class ANRootView(tk.Frame):
    """
    Root view potentially containing multiple different top level views (ie. login or main anchor view).
    """
    def __init__(self, 
                 master, 
                 engine: ANEngineInterface):
        super().__init__(master)

        self._engine = weakref.ref(engine)

        self.anchor_settings = ANAnchorSettings(self, engine)

        self.activate_hotkeys_button = tk.Button(self.master, text="Activate hotkeys", command=self.activate_hotkeys)
        self.activate_hotkeys_button.grid(column=2, sticky='e', padx=5, pady=(0, 3))

    def activate_hotkeys(self):
        self._engine().get_anchors_controller().activate_hotkeys()

    