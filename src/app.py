
import ctypes
import logging
import customtkinter as ctk

import keyboard

from src.common.config import SCREEN_HEIGHT, SCREEN_WIDTH, TASKBAR_ICON_PATH, TITLE_STR
from src.engine.engine import ANEngine
from src.ui.root_view import ANRootView
from src.ui.tray import ANTray


class App(object):
    def __init__(self):
        logging.basicConfig(filename='error.log', level=logging.INFO)
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(TITLE_STR)
        
        self.root = ctk.CTk()
        self.root.title(TITLE_STR)
        self.root.protocol("WM_DELETE_WINDOW", self.hide_window)
        self.root.geometry(f'{SCREEN_WIDTH}x{SCREEN_HEIGHT}')
        self.root.minsize(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.root.iconbitmap(default=TASKBAR_ICON_PATH)

        self._root_view = None

        self._engine = ANEngine(self.root)

    def run(self):
        self._engine.load()
        self._root_view = ANRootView(self.root, self._engine)
        self._tray = ANTray(self)
        self.root.mainloop()
    
    def show_window(self) -> None:
        self.root.after(0, self.root.deiconify)
    
    def hide_window(self) -> None:
        self.root.after(0, self.root.withdraw)

    def exit(self) -> None:
        keyboard.unhook_all()
        self.root.destroy()