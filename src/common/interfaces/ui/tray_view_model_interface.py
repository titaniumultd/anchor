
from abc import ABC, abstractmethod


class ANTrayViewModelInterface(ABC):

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def show_config_window(self):
        pass

    @abstractmethod
    def hide_config_window(self):
        pass

    @abstractmethod
    def exit_app(self):
        pass

    @abstractmethod
    def get_global_hotkey_state(self) -> bool:
        pass

    @abstractmethod
    def toggle_global_hotkey_state(self):
        pass