
import logging
import tkinter as tk

from src.common.singleton import ANSingleton
from src.engine.engine import ANEngine
from src.ui.root_view import ANRootView


class App(object):
    def __init__(self):
        logging.basicConfig(filename='error.log', level=logging.INFO)
        
        self.root = tk.Tk()
        self.root.title("Anchor")
        self._root_view = None

        self._engine = ANEngine(self.root)

    def run(self):
        self._engine.load()
        self._root_view = ANRootView(self.root, self._engine)

        self.root.mainloop()