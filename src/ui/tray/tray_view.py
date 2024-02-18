import threading
import weakref

import pystray as tray
from PIL import Image

from src.common.interfaces.ui.tray_view_model_interface import ANTrayViewModelInterface
from src.common.variables import TASKBAR_ICON_PATH, TITLE_STR


class ANTrayView(object):
    """
    Object to wrap the system tray menu
    """

    def __init__(self, view_model: ANTrayViewModelInterface):
        self._view_model = weakref.ref(view_model)

        self._global_hotkey_state = True
        self._tray_menu = tray.Menu(
            tray.MenuItem("Show", self._show_config_window), 
            tray.MenuItem("Hide", self._hide_config_window),
            tray.MenuItem("Hotkeys Enabled", self._toggle_global_hotkeys, checked=self._get_hotkey_state),
            tray.MenuItem("Exit", self._exit)
            )
        self._tray_icon = tray.Icon("title", Image.open(TASKBAR_ICON_PATH), TITLE_STR, self._tray_menu)

        threading.Thread(target=self._tray_icon.run, kwargs={'setup':self._show_config_window}, daemon=True).start() # macOS / linux incompatible

    def _get_hotkey_state(self) -> bool:
        vm = self._view_model()
        return vm.get_global_hotkey_state()

    def _show_config_window(self, icon):
        self._tray_icon.visible = True

        vm = self._view_model()
        vm.show_config_window()

    def _hide_config_window(self):
        vm = self._view_model()
        vm.hide_config_window()
    
    def _toggle_global_hotkeys(self):
        vm = self._view_model()
        vm.toggle_global_hotkey_state()
    
    def _exit(self):
        self._tray_icon.visible = False

        vm = self._view_model()
        vm.exit_app()