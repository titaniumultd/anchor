

class ANConfigModel(object):
    def __init__(self):

        self._global_hotkeys_state:bool = True
        self._tray_enabled:bool = True
        self._config_view_visible:bool = True

    def toggle_global_hotkeys_state(self) -> bool:
        self._global_hotkeys_state = not self._global_hotkeys_state
        return self._global_hotkeys_state
    
    def get_tray_enabled(self) -> bool:
        return self._tray_enabled
    
    def get_config_view_visible(self) -> bool:
        return self._config_view_visible

    def set_tray_enabled(self, state: bool) -> bool:
        self._tray_enabled = state
    
    def set_config_view_visible(self, state: bool) -> bool:
        self._config_view_visible = state