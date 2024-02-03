import keyboard
import logging
import ctypes
import tkinter as tk

from src.common.config import SCREEN_WIDTH, SCREEN_HEIGHT, TASKBAR_ICON_PATH
from src.engine.engine import ANEngine
from src.ui.root_view import ANRootView


class App(object):
    def __init__(self):
        logging.basicConfig(filename='error.log', level=logging.INFO)
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("myappid")
        
        self.root = tk.Tk()
        self.root.title("Anchor")
        self.root.protocol("WM_DELETE_WINDOW", self._close_window)
        self.root.geometry(f'{SCREEN_WIDTH}x{SCREEN_HEIGHT}')
        self.root.minsize(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.root.iconbitmap(default=TASKBAR_ICON_PATH)

        self._root_view = None

        self._engine = ANEngine(self.root)

    def run(self):
        self._engine.load()
        self._root_view = ANRootView(self.root, self._engine)
        self.root.mainloop()
        
    def _close_window(self) -> None:
        keyboard.unhook_all()
        self.root.destroy()
