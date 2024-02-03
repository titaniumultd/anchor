import threading

import pystray as tray
from PIL import Image

from src.common.config import TASKBAR_ICON_PATH


class ANTray(object):
    """
    Object to wrap the system tray icon
    """

    def __init__(self, app):
        self.app = app
        self.tray_menu = tray.Menu(
            tray.MenuItem("Show", self._show_window), 
            tray.MenuItem("Hide", self._hide_window), 
            tray.MenuItem("Exit", self._exit)
            )
        self.tray = tray.Icon("title", Image.open(TASKBAR_ICON_PATH), "Anchor", self.tray_menu)

        threading.Thread(target=self.tray.run, kwargs={'setup':self._show_window}, daemon=True).start() # macOS / linux incompatible

    def _show_window(self, icon) -> None:
        self.tray.visible = True
        self.app.show_window()

    def _hide_window(self) -> None:
        self.app.hide_window()
    
    def _exit(self) -> None:
        self.tray.visible = False
        self.app.exit()