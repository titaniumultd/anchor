
from src.common.variables import ACTION_LEFT_CLICK


class ANAnchor(object):
        
        def __init__(self) -> object:
            self._anchor_position: tuple[int,int] = None
            self._action: str = ACTION_LEFT_CLICK
            self._hotkeys: dict[['record', 'click']:str] = {
                'record': 'undefined',
                'click': 'undefined'
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