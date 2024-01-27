import json
import logging
import tkinter as tk
from tkinter import ttk
from pathlib import Path

from pynput.mouse import Controller as MouseController

from src.common.anchor import ANAnchor
from src.common.singleton import ANSingleton
from src.common.notifier import ANNotifier

logging.basicConfig(filename='error.log', level=logging.INFO)
MAX_ANCHORS = 5


class App(ANSingleton):
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Anchor")
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)
        self.root.grid_rowconfigure(0, weight=1)

        self.notifier = ANNotifier()
        self.notifier.register_listener(self)

        self.mouse = MouseController()

        self.state_file_path = Path('config/state.json')
        self.ensure_state_file_exists()

        self.current_profile = 'default'
        self.anchors = []

        self.add_anchor_button = tk.Button(self.root, text="New Anchor", command=self.drop_an_anchor)
        self.activate_hotkeys_button = tk.Button(self.root, text="Activate hotkeys", command=self.activate_hotkeys)

        self.profiles_combobox = ttk.Combobox(self.root, width=10)
        self.new_profile_button = tk.Button(self.root, text="New Profile", command=self.create_new_profile)
        self.delete_profile_button = tk.Button(self.root, text="Delete Profile", command=self.delete_profile)

        self.profiles_combobox.bind("<<ComboboxSelected>>", self.switch_profile)

    def run(self):
        self.profiles_combobox.grid(row=0, column=0)
        self.new_profile_button.grid(row=0, column=0, sticky="w")
        self.delete_profile_button.grid(row=0, column=0, padx=15, sticky="e")

        self.add_anchor_button.grid(row=1, column=0, sticky='w', padx=5, pady=(20, 0))
        self.activate_hotkeys_button.grid(row=1, column=0, sticky='e', padx=5, pady=(20, 0))

        if self.load_state():
            self.activate_hotkeys()
        if len(self.anchors) == 0:
            self.drop_an_anchor()

        self.root.mainloop()

    def drop_an_anchor(self):
        if len(self.anchors) >= MAX_ANCHORS:
            return
        new_anchor = ANAnchor(self.root, len(self.anchors), self.mouse, self.notifier)
        new_anchor.remove_anchor_button['command'] = lambda anchor=new_anchor: self.remove_anchor(anchor)
        self.anchors.append(new_anchor)

        self.save_state()

    def remove_anchor(self, anchor):
        index = self.anchors.index(anchor)
        self.anchors.remove(anchor)
        anchor.destroy()

        for i in range(index, len(self.anchors)):
            self.anchors[i].index = i

        self.save_state()

    def activate_hotkeys(self):
        for anchor in self.anchors:
            anchor.record_hotkey.activate()
            anchor.click_hotkey.activate()

    def ensure_state_file_exists(self):
        if not self.state_file_path.exists():
            self.state_file_path.parent.mkdir(parents=True, exist_ok=True)
            state = {
                'last_profile': 'default',
                'profiles': {'default': []}
            }
            with self.state_file_path.open('w') as file:
                json.dump(state, file, default=str)

    def read_state_file(self):
        with self.state_file_path.open('r') as file:
            return json.load(file)

    def write_state_file(self, state):
        with self.state_file_path.open('w') as file:
            json.dump(state, file, default=str)

    def load_state(self):
        state = self.read_state_file()

        self.profiles_combobox['values'] = list(state['profiles'].keys())
        self.profiles_combobox.set(state['last_profile'])

        if 'profiles' in state:
            self.current_profile = state['last_profile']
            profiles = state['profiles']
            if self.current_profile in profiles:
                anchors = profiles[self.current_profile]
                for anchor_dict in anchors:
                    new_anchor = ANAnchor.from_dict(anchor_dict, self.root, self.mouse, self.notifier)
                    new_anchor.remove_anchor_button['command'] = lambda anchor=new_anchor: self.remove_anchor(anchor)
                    self.anchors.append(new_anchor)
            else:
                logging.error(f"No such profile: {self.current_profile}")
        else:
            logging.error("Invalid state.json format. Expected a dictionary with 'profiles' key.")

    def save_state(self):
        state = self.read_state_file()

        if 'profiles' in state:
            state['profiles'][self.current_profile] = [anchor.to_dict() for anchor in self.anchors]
            state['last_profile'] = self.current_profile
            self.write_state_file(state)
        else:
            logging.error("Invalid state.json format in save_state. Expected a dictionary with 'profiles' key.")

    def update(self):
        self.save_state()

    def get_profiles(self):
        state = self.read_state_file()
        return state.get('profiles', {})

    def add_profile(self, profile_name):
        state = self.read_state_file()
        state['profiles'][profile_name] = []
        state['last_profile'] = profile_name
        self.write_state_file(state)

    def create_new_profile(self):
        new_profile_name = f"profile{len(self.profiles_combobox['values']) + 1}"
        self.add_profile(new_profile_name)

        profiles = self.get_profiles()
        self.profiles_combobox['values'] = list(profiles.keys())
        self.profiles_combobox.set(new_profile_name)

    def delete_profile(self):
        selected_profile = self.profiles_combobox.get()
        if selected_profile == 'default':
            return

        state = self.read_state_file()
        del state['profiles'][selected_profile]
        self.write_state_file(state)

        self.profiles_combobox['values'] = list(state['profiles'].keys())
        self.profiles_combobox.set('default')
        self.switch_profile()

    def switch_profile(self, event=None):
        selected_profile = self.profiles_combobox.get()

        if selected_profile == self.current_profile:
            return

        for anchor in self.anchors:
            anchor.destroy(save=False)
        self.anchors.clear()

        state = self.read_state_file()
        if 'profiles' in state:
            profiles = state['profiles']
            if selected_profile in profiles:
                self.current_profile = selected_profile
                state['last_profile'] = selected_profile
                anchors = profiles[selected_profile]

                for anchor_dict in anchors:
                    new_anchor = ANAnchor.from_dict(anchor_dict, self.root, self.mouse, self.notifier)
                    new_anchor.remove_anchor_button['command'] = lambda anchor=new_anchor: self.remove_anchor(anchor)
                    self.anchors.append(new_anchor)

                self.write_state_file(state)
            else:
                logging.error(f"No such profile: {selected_profile}")
        else:
            logging.error("Invalid state.json format in switch_profile. Expected a dictionary with 'profiles' key.")
