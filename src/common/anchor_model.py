
from src.common.interfaces.anchor_model_interface import ANAnchorModelInterface


class ANAnchor(ANAnchorModelInterface, object):
        
        def __init__(self) -> object:
            self._anchor_position: tuple[int,int] = None
            self._action: str = None
            self._hotkeys: dict[str:str] = {
                'record': None,
                'click': None
            }
        
        def get_position(self) -> tuple[int,int]:
            return self._anchor_position
        
        def get_action(self) -> str:
            return self._action
        
        def get_hotkey(self, hotkey_type: str) -> str:
            return self._hotkeys[hotkey_type]
        
        def set_anchor_position(self, position: tuple[int,int]):
            self._anchor_position = position
        
        def set_hotkey(self, hotkey_type: str, key_combo: str):
            self._hotkeys[hotkey_type] = key_combo
        
        def set_action(self, action: str):
            self._action = action