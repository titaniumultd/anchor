import tkinter as tk
from anchor import Anchor
from pynput.mouse import Controller as MouseController

class App:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Anchor")
        self.root.grid_columnconfigure(0, weight=1)  # adjust size with window
        self.root.grid_columnconfigure(1, weight=1)  # adjust size with window
        self.root.grid_rowconfigure(0, weight=1)

        self.mouse = MouseController()

        self.anchors = []

        self.add_anchor_button = tk.Button(self.root, text="New Anchor", command=self.drop_an_anchor)
        self.activate_hotkeys_button = tk.Button(self.root, text="Activate hotkeys", command=self.activate_hotkeys)

    def run(self):
        self.add_anchor_button.grid(row=0, column=0, sticky='w', padx=5)
        self.activate_hotkeys_button.grid(row=0, column=0, sticky='e', padx=5)

        self.drop_an_anchor()
        self.root.mainloop()

    def drop_an_anchor(self):
        if len(self.anchors) >= 5:  # maximum of 5 anchors
            return
        new_anchor = Anchor(self.root, len(self.anchors), self.mouse)
        new_anchor.remove_anchor_button['command'] = lambda: self.remove_anchor(new_anchor)
        new_anchor.grid_ui_elements()
        self.anchors.append(new_anchor)

    def remove_anchor(self, anchor):
        index = self.anchors.index(anchor)
        self.anchors.remove(anchor)
        anchor.destroy()

        # Shift down the remaining anchors
        for i in range(index, len(self.anchors)):
            self.anchors[i].index = i
            self.anchors[i].grid_ui_elements()

    def activate_hotkeys(self):
        for anchor in self.anchors:
            anchor.record_hotkey.activate()
            anchor.click_hotkey.activate()

app = App()
app.run()