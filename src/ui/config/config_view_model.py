
import customtkinter as ctk

from src.common.interfaces.ui.config_view_model_interface import ANConfigViewModelInterface
from src.common.interfaces.engine_interface import ANEngineInterface


class ANConfigViewModel(ANConfigViewModelInterface, object):
    def __init__(self, 
                engine: ANEngineInterface
                ): 

        self._config_model = engine.get_config_model()
        self.hotkey_var = ctk.BooleanVar(value=True)

    def update(self):
        if self._config_model.get_global_hotkey_state():
            self.hotkey_var.set(True)
        else:
            self.hotkey_var.set(False)

    def toggle_global_hotkey_state(self):
        self._config_model.toggle_global_hotkey_state()
        self.update()