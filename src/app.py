
import ctypes
import logging


from src.common.variables import TITLE_STR
from src.engine.engine import ANEngine
from src.ui.anchor.anchor_view_model import ANViewModel



class App(object):
    def __init__(self):
        logging.basicConfig(filename='error.log', level=logging.INFO)
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(TITLE_STR)
        
        self._model = ANEngine()
        self._view_model = ANViewModel(self._model)

    def run(self):
        self._model.load()
        self._view_model.load_view()