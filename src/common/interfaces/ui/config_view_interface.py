

from abc import ABC, abstractmethod

class ANConfigViewInterface(ABC):

    @abstractmethod
    def show_window(self):
        pass

    @abstractmethod
    def hide_window(self):
        pass

    @abstractmethod
    def exit_app(self):
        pass