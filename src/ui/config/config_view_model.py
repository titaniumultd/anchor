
import customtkinter as ctk
import weakref

from src.common.interfaces.ui.config_view_model_interface import ANConfigViewModelInterface
from src.common.interfaces.config_model_interface import ANConfigModelInterface
from src.common.interfaces.ui.config_view_interface import ANConfigViewInterface
from src.common.interfaces.anchor_model_interface import ANAnchorModelInterface
from src.common.interfaces.engine_interface import ANEngineInterface
from src.ui.config.config_view import ANConfigView
from src.common.interfaces.controllers.anchor_controller_interface import ANAnchorControllerInterface


class ANConfigViewModel(ANConfigViewModelInterface, object):
    def __init__(self, 
                engine: ANEngineInterface,
                root: ctk.CTk,
                config_model: ANConfigModelInterface,
                anchor_controller: ANAnchorControllerInterface
                ):
        
        self._engine = weakref.ref(engine)
        self._root = root      
        self._config_model = config_model
        self._anchor_controller = anchor_controller

        self._view:ANConfigViewInterface = ANConfigView(self._root, self)
        self._global_hotkey_state:ctk.IntVar = ctk.IntVar(self._config_model.get_global_hotkey_state())

        self._root.protocol("WM_DELETE_WINDOW", self.hide_window)

    def update(self):
        if self._config_model.get_global_hotkey_state():
            self._global_hotkey_state.set(1)
        else:
            self._global_hotkey_state.set(0)

    def toggle_global_hotkeys_enabled(self):
        self._config_model.toggle_global_hotkey_state()
        self._get_engine().update()

    def get_anchors(self) -> list[ANAnchorModelInterface]:
        return self._anchor_controller.get_anchors()
    
    def show_window(self):
        self._root.deiconify()

    def hide_window(self):
        self._root.iconify()
    
    def exit_app(self):
        self._root.destroy()
    
    def _get_engine(self) -> ANEngineInterface:
        return self._engine()