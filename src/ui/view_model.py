
from abc import ABC

from src.common.interfaces.engine_interface import ANEngineInterface
from src.common.interfaces.view_interface import ANViewInterface

class ANViewModel(ABC):
    def __init__(self, model: ANEngineInterface, view:ANViewInterface):
        self._model = model
        self._view = view
    
    def load(self):
        self._view.load()
    
    def toggle_hotkeys(self):
        self._model.get_anchors_controller().toggle_hotkeys()