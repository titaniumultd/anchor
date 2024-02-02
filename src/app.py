
import logging
import tkinter as tk

from src.common.config import SCREEN_WIDTH, SCREEN_HEIGHT
from src.engine.engine import ANEngine
from src.ui.root_view import ANRootView


class App(object):
    def __init__(self):
        logging.basicConfig(filename='error.log', level=logging.INFO)
        
        self.root = tk.Tk()
        self.root.title("Anchor")
        self.root.geometry(f'{SCREEN_WIDTH}x{SCREEN_HEIGHT}')
        self.root.minsize(SCREEN_WIDTH, SCREEN_HEIGHT)

        self._root_view = None

        self._engine = ANEngine(self.root)

    def run(self):
        self._engine.load()
        self._root_view = ANRootView(self.root, self._engine)

        self.root.mainloop()