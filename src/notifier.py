class Notifier:

    def __init__(self) -> None:
        self.listeners = []

    def register_listener(self, listener):
        self.listeners.append(listener)

    def notify(self):
        for listener in self.listeners:
            listener.update()