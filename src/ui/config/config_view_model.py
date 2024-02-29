
import customtkinter as ctk
from src.common.config_model import ANConfigModel

from src.common.interfaces.ui.config_view_model_interface import ANConfigViewModelInterface


class ANConfigViewModel(ANConfigViewModelInterface, object):
    def __init__(self, 
                config_model: ANConfigModel
                ): 

        self._config_model = config_model
        self._hotkey_var = ctk.BooleanVar(value=True)

    def update(self):
        if self._config_model.get_global_hotkey_state():
            self.hotkey_var.set(True)
        else:
            self.hotkey_var.set(False)

    def toggle_global_hotkey_state(self):
        self._config_model.toggle_global_hotkey_state()
        self.update()

    @property
    def hotkey_var(self) -> ctk.BooleanVar:
        return self._hotkey_var