
from customtkinter import CTk

from src.common.interfaces.anchor_model_interface import ANAnchorModelInterface
from src.common.interfaces.ui.anchor_view_interface import ANAnchorViewInterface
from src.common.interfaces.ui.anchor_view_model_interface import ANAnchorViewModelInterface
from src.common.interfaces.controllers.anchor_controller_interface import ANAnchorsControllerInterface
from src.ui.anchor.anchor_view import ANAnchorView


class ANAnchorViewModel(ANAnchorViewModelInterface, object):

    def __init__(self, 
                 root: CTk,
                 anchor: ANAnchorModelInterface, 
                 anchor_controller: ANAnchorsControllerInterface
                 ):
        
        self._anchor = anchor
        self._root = root
        self._anchor_controller = anchor_controller

        self._view:ANAnchorViewInterface = ANAnchorView(self._root, self)
    
    def update_action(self, action:str):
        self._anchor.set_action(action)

    def request_hotkey_update(self, hotkey:str):
        self._anchor_controller.update_hotkey(self._anchor, hotkey)

    def update(self, view: ANAnchorViewInterface):
        update_packet = {
            'anchor_index' : self._anchor_controller.get_anchor_index(self._anchor),
            'record_hotkey_combo' : self._anchor.get_hotkey('record'),
            'click_hotkey_combo' : self._anchor.get_hotkey('click'),
            'anchor_action' : self._anchor.get_action()
        }

        view.update(update_packet)