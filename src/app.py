
import ctypes
import logging

from customtkinter import CTk

from src.common.interfaces.engine_interface import ANEngineInterface
from src.common.interfaces.ui.config_view_interface import ANConfigViewInterface

from src.common.variables import TITLE_STR

from src.engine.engine import ANEngine
from src.ui.config.config_view import ANConfigView
from src.ui.tray.tray import ANTray


class App(object):
    def __init__(self):
        logging.basicConfig(filename='error.log', level=logging.INFO)
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(TITLE_STR)

        self._master = CTk()
        self._engine = ANEngine()
        self._config_view = ANConfigView(self._master, self._engine)
        self._tray = ANTray(self._engine.get_config_model(), self._config_view)
    
    def run(self):
        self._master.mainloop()