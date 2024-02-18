
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
    def __init__(self, engine: ANEngineInterface):
        
        self._engine = weakref.ref(engine)
        
        self._config_model:ANConfigModelInterface = self._get_engine().get_config_model()
        self._anchor_controller:ANAnchorControllerInterface = self._get_engine().get_anchors_controller()

        self._root:ctk.CTk = self._get_engine().get_root()
        self._view:ANConfigViewInterface = ANConfigView(self._root)
        self._global_hotkey_state:ctk.StringVar = ctk.StringVar(self._config_model.get_global_hotkey_state())

    def toggle_global_hotkeys_enabled(self):
        self._config_model.toggle_global_hotkey_state()
    
    def get_global_hotkey_state(self) -> bool:
        state = self._config_model.get_global_hotkey_state()
        self._global_hotkey_state.set(state)
        return state

    def get_anchors(self) -> list[ANAnchorModelInterface]:
        return self._anchor_controller.get_anchors()
    
    def show_window(self):
        self._root.deiconify()

    def hide_window(self):
        self._root.iconify()
    
    def exit_app(self):
        self._get_engine().exit_app()
    
    def _get_engine(self) -> ANEngineInterface:
        return self._engine()