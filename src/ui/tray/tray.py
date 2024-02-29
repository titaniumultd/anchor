
import threading
import weakref

import pystray as tray
from PIL import Image

from src.common.interfaces.ui.config_view_interface import ANConfigViewInterface
from src.common.variables import TASKBAR_ICON_PATH, TITLE_STR
from src.common.config_model import ANConfigModel


class ANTray(object):
    """
    Object to wrap the system tray menu
    """

    def __init__(self,
                app,
                config_view: ANConfigViewInterface,
                config_model: ANConfigModel):
        
        self._app = weakref.ref(app)
        self._config_view = weakref.ref(config_view)
        self._config_model = config_model
        
        self._tray_menu = tray.Menu(
            tray.MenuItem("Show", self._show_config_window), 
            tray.MenuItem("Hide", self._hide_config_window),
            tray.MenuItem("Hotkeys Enabled", self._toggle_global_hotkeys, checked=self._get_hotkey_state),
            tray.MenuItem("Exit", self._exit)
            )
        self._tray_icon = tray.Icon("title", Image.open(TASKBAR_ICON_PATH), TITLE_STR, self._tray_menu)

        threading.Thread(target=self._tray_icon.run, kwargs={'setup':self._show_config_window}, daemon=True).start() # macOS / linux incompatible

    def update(self):
        self._tray_icon.update_menu()

    def _get_hotkey_state(self, menu_item:str) -> bool:
        return self._config_model.get_global_hotkey_state()

    def _show_config_window(self, icon):
        self._tray_icon.visible = True
        self._config_view().show_window()

    def _hide_config_window(self):
        self._config_view().hide_window()
    
    def _toggle_global_hotkeys(self):
        self._config_view().toggle_global_hotkeys()
    
    def _exit(self):
        self._tray_icon.visible = False
        self._app().exit_app()