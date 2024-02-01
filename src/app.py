
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

        # self.profiles_combobox = ttk.Combobox(self.root, width=10)
        # self.new_profile_button = tk.Button(self.root, text="New Profile", command=self.create_new_profile)
        # self.delete_profile_button = tk.Button(self.root, text="Delete Profile", command=self.delete_profile)

        # self.profiles_combobox.bind("<<ComboboxSelected>>", self.switch_profile)

    def run(self):
        self.activate_hotkeys_button.grid(row=1, column=0, sticky='e', padx=5, pady=(20, 0))

        self._engine.load()

        self.root.mainloop()

    def activate_hotkeys(self):
        for anchor in self.anchors:
            anchor.record_hotkey.activate()
            anchor.click_hotkey.activate()

    @property
    def anchors(self):
        return self._engine.get_anchors_controller().get_anchors()