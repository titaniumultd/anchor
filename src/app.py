
import ctypes
import logging
from customtkinter import CTk

from src.common.variables import TITLE_STR
from src.engine.engine import ANEngine


class App(object):
    def __init__(self):
        logging.basicConfig(filename='error.log', level=logging.INFO)
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(TITLE_STR)

        self._root = CTk()
        
        self._engine = ANEngine(self._root)
    
    def run(self):
        self._engine.load()