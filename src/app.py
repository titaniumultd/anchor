
import ctypes
import logging

from customtkinter import CTk

from src.common.variables import TITLE_STR
from src.engine.engine import ANEngine
from src.ui.config.config_view import ANConfigView
from src.common.interfaces.ui.config_view_interface import ANConfigViewInterface
from src.common.interfaces.engine_interface import ANEngineInterface
from src.ui.tray.tray_view import ANTrayView
from src.common.interfaces.ui.tray_view_interface import ANTrayViewInterface


class App(object):
    def __init__(self):
        logging.basicConfig(filename='error.log', level=logging.INFO)
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(TITLE_STR)

        self._master = CTk()
        self._engine:ANEngineInterface = ANEngine()
        self._config_view:ANConfigViewInterface = ANConfigView(self._master, self._engine)
        #self._tray_view:ANTrayViewInterface = ANTrayView()
    
    def run(self):
        self._master.mainloop()