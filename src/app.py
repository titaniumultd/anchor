from typing import Any
import keyboard
import logging
import ctypes
import threading
import pystray as tray
import tkinter as tk

from PIL import Image

from src.common.config import SCREEN_WIDTH, SCREEN_HEIGHT, TASKBAR_ICON_PATH
from src.engine.engine import ANEngine
from src.ui.root_view import ANRootView


class App(object):
    def __init__(self):
        logging.basicConfig(filename='error.log', level=logging.INFO)
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("anchor")
        
        self.root = tk.Tk()
        self.root.title("Anchor")
        self.root.protocol("WM_DELETE_WINDOW", self._hide_window)
        self.root.geometry(f'{SCREEN_WIDTH}x{SCREEN_HEIGHT}')
        self.root.minsize(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.root.iconbitmap(default=TASKBAR_ICON_PATH)
        self.tray_menu = tray.Menu(
            tray.MenuItem("Show", self._show_window), 
            tray.MenuItem("Hide", self._hide_window), 
            tray.MenuItem("Exit", self._exit_from_tray)
            )
        self.tray = tray.Icon("title", Image.open(TASKBAR_ICON_PATH), "Anchor", self.tray_menu)

        self._root_view = None

        self._engine = ANEngine(self.root)

    def run(self):
        self._engine.load()
        self._root_view = ANRootView(self.root, self._engine)
        threading.Thread(target=self.tray.run, kwargs={'setup':self._show_window}, daemon=True).start() # macOS/Linux incompatible
        self.root.mainloop()
    
    def _show_window(self, icon) -> None:
        self.tray.visible = True
        self.root.after(0, self.root.deiconify)
    
    def _hide_window(self) -> None:
        self.root.after(0, self.root.withdraw)
        
    def _close_window(self) -> None:
        self.root.iconify()

    def _exit_from_tray(self) -> None:
        keyboard.unhook_all()
        self.tray.visible = False
        self.root.destroy()