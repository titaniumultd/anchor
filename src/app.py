import keyboard
import logging
import tkinter as tk

from pynput.mouse import Controller as MouseController

from src.common.notifier import ANNotifier
from src.common.singleton import ANSingleton
from src.engine.engine import ANEngine
from src.ui.root_view import ANRootView


class App(object):
    def __init__(self):
        logging.basicConfig(filename='error.log', level=logging.INFO)
        
        self.root = tk.Tk()
        self.root.title("Anchor")
        self.root.protocol("WM_DELETE_WINDOW", self._close_window)
        self.root.geometry(f'{SCREEN_WIDTH}x{SCREEN_HEIGHT}')
        self.root.minsize(SCREEN_WIDTH, SCREEN_HEIGHT)

        self._root_view = None

        self._engine = ANEngine(self.root)

    def run(self):
        self._engine.load()
        self._root_view = ANRootView(self.root, self._engine)
        self.root.mainloop()
        
    def _close_window(self) -> None:
        keyboard.unhook_all()
        self.root.destroy()
