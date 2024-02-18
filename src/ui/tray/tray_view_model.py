

from src.common.interfaces.ui.config_view_model_interface import ANConfigViewModelInterface
from src.ui.tray.tray_view import ANTrayView
from src.common.interfaces.ui.tray_view_interface import ANTrayViewInterface
from src.common.interfaces.ui.tray_view_model_interface import ANTrayViewModelInterface


class ANTrayViewModel(ANTrayViewModelInterface, object):
    def __init__(self, config_view_model: ANConfigViewModelInterface) -> object:
        self._config_view_model = config_view_model

        self._view:ANTrayViewInterface = ANTrayView(self)

    def toggle_global_hotkey_state(self):
        self._config_view_model.toggle_global_hotkey_state()

    def show_config_window(self):
        self._config_view_model.show_window()

    def hide_config_window(self):
        self._config_view_model.hide_window()
    
    def exit_app(self):
        self._config_view_model.exit_app()
    
    def get_global_hotkey_state(self) -> bool:
        return self._config_view_model.get_global_hotkey_state()