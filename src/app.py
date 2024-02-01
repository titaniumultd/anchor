
import logging
import tkinter as tk

from pynput.mouse import Controller as MouseController

from src.common.notifier import ANNotifier
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

        self.notifier = ANNotifier()
        self.notifier.register_listener(self)

        self.mouse = MouseController()

        self._engine = ANEngine(self.root, self.mouse, self.notifier)

        #self.activate_hotkeys_button = tk.Button(self.root, text="Activate hotkeys", command=self.activate_hotkeys) # replace with global activation tickbox

    def run(self):
        #self.activate_hotkeys_button.grid(row=1, column=0, sticky='e', padx=5, pady=(20, 0))

        self._engine.load()

        self.root.mainloop()

    def activate_hotkeys(self):
        for anchor in self.anchors:
            anchor.record_hotkey.activate()
            anchor.click_hotkey.activate()

    def update(self):
        self._engine.get_anchors_controller().save_anchors()

    @property
    def anchors(self):
        return self._engine.get_anchors_controller().get_anchors()