
from customtkinter import CTk

from src.common.interfaces.config_view_model_interface import ANConfigViewModelInterface
from src.common.interfaces.config_model_interface import ANConfigModelInterface
from src.common.interfaces.config_view_interface import ANConfigViewInterface
from src.common.interfaces.anchor_model_interface import ANAnchorModelInterface
from src.ui.config.config_view import ANConfigView
from src.common.interfaces.anchors_interface import ANAnchorsControllerInterface


class ANConfigViewModel(ANConfigViewModelInterface, object):
    def __init__(self, root: CTk, config_model:  ANConfigModelInterface):

        self._root = root
        self._config_model = config_model

        self._anchor_controller:ANAnchorsControllerInterface = self._load_anchor_controller()
        self._view: ANConfigViewInterface = ANConfigView(self._root)

    def update(self):
        packet = {
            'hotkey_state': self._config_model.get_global_hotkey_state()
        }
        self._view.update(packet)

    def toggle_global_hotkeys_enabled(self):
        self._config_model.toggle_global_hotkey_state()    

    def get_anchors(self) -> list[ANAnchorModelInterface]:
        return self._anchor_controller.get_anchors()
        
    def _load_anchor_controller(self) -> ANAnchorsControllerInterface:
        return self._config_model.get_anchor_controller()