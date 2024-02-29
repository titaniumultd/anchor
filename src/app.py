
import ctypes
import logging

from customtkinter import CTk

from src.common.variables import TITLE_STR

from src.engine.engine import ANEngine
from src.ui.config.config_view import ANConfigView


class App(object):
    def __init__(self):
        logging.basicConfig(filename='error.log', level=logging.INFO)
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(TITLE_STR)

        self._master = CTk()
        self._engine = ANEngine()
        self._config_view = ANConfigView(self, self._master, self._engine)
    
    def run(self):
        self._master.mainloop()
    
    def exit_app(self):
        self._master.destroy()