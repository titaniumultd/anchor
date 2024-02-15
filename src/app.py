
import ctypes
import logging


from src.common.config import SCREEN_HEIGHT, SCREEN_WIDTH, TASKBAR_ICON_PATH, TITLE_STR
from src.engine.engine import ANEngine
from src.ui.view_model import ANViewModel
from src.ui.view.view import ANRootView



class App(object):
    def __init__(self):
        logging.basicConfig(filename='error.log', level=logging.INFO)
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(TITLE_STR)
        
        self._model = ANEngine()
        self._view = ANRootView()
        self._view_model = ANViewModel(self._model, self._view)

    def run(self):
        self._model.load()
        self._view_model.load()