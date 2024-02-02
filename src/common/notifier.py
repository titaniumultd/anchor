
from abc import ABC, abstractmethod

class ANNotifyListener(ABC):
    """
    Notify abstract class called from ANNotifer.
    """
    @abstractmethod
    def update(self):
        """
        Placeholder method called to ANNotifyListener objects.
        """
        pass


class ANNotifier:
    """
    Broadcasting notification class.
    """
    def __init__(self) -> None:
        self.listeners = []

    def register_listener(self, listener: ANNotifyListener):
        self.listeners.append(listener)

    def notify(self):
        for listener in self.listeners:
            listener.update()