

from abc import ABC, abstractmethod

from src.common.interfaces.anchor_model_interface import ANAnchorModelInterface

class ANConfigViewModelInterface(ABC):

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def toggle_global_hotkey_state(self):
        pass   

    @abstractmethod
    def get_anchors(self) -> list[ANAnchorModelInterface]:
        pass

    @abstractmethod
    def show_window(self):
        pass

    @abstractmethod
    def hide_window(self):
        pass

    @abstractmethod
    def exit_app(self):
        pass