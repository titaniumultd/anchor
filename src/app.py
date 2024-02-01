
import logging
import tkinter as tk

from src.common.singleton import ANSingleton
from src.engine.engine import ANEngine


class App(ANSingleton):
    def __init__(self):
        logging.basicConfig(filename='error.log', level=logging.INFO)
        
        self.root = tk.Tk()
        self.root.title("Anchor")

        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)
        self.root.grid_rowconfigure(0, weight=1)

        self._engine = ANEngine(self.root)

        self.activate_hotkeys_button = tk.Button(self.root, text="Activate hotkeys", command=self.activate_hotkeys)

    def run(self):
        self.activate_hotkeys_button.grid(row=1, column=0, sticky='e', padx=5, pady=(20, 0))

        self._engine.load()

        self.root.mainloop()

    def activate_hotkeys(self):
        self._engine.get_anchors_controller().activate_hotkeys()

    @property
    def anchors(self):
        return self._engine.get_anchors_controller().get_anchors()