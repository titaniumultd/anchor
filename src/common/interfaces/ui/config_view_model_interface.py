

from abc import ABC, abstractmethod

from customtkinter import BooleanVar


class ANConfigViewModelInterface(ABC):

    def __init__(self):
        self.hotkey_var: BooleanVar

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def toggle_global_hotkey_state(self):
        pass   