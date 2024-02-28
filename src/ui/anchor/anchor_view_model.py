 
import customtkinter as ctk

from src.common.interfaces.ui.anchor_view_model_interface import ANAnchorViewModelInterface
from src.common.interfaces.controllers.anchor_controller_interface import ANAnchorControllerInterface

from src.common.anchor_model import ANAnchor


class ANAnchorViewModel(ANAnchorViewModelInterface, object):

    def __init__(self, 
                 anchor: ANAnchor, 
                 anchor_controller: ANAnchorControllerInterface
                 ):
        
        self._anchor = anchor
        self._anchor_controller = anchor_controller

        self.record_hotkey_strvar: ctk.StringVar = ctk.StringVar(value=self._anchor.get_hotkey('record'))
        self.click_hotkey_strvar: ctk.StringVar = ctk.StringVar(value=self._anchor.get_hotkey('click'))
        self.anchor_action: str = self._anchor.get_action()

    def update_action(self, action:str):
        self._anchor.set_action(action)

    def request_hotkey_update(self, hotkey_type:str):
        self._anchor_controller.update_hotkey(self._anchor, hotkey_type, self.update)

    def update(self):
        self.record_hotkey_strvar.set(self._anchor.get_hotkey('record'))
        self.click_hotkey_strvar.set(self._anchor.get_hotkey('click'))