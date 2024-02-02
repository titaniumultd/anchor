
import threading
import weakref

from pynput.mouse import Button as MouseButton

from src.common.interfaces.engine_interface import ANEngineInterface
from src.common.hotkey import ANHotKey
from src.common.config import ACTION_LEFT_CLICK, ACTION_RIGHT_CLICK      
        

class ANAnchor(object):

    ACTIONS = [
        ACTION_LEFT_CLICK, 
        ACTION_RIGHT_CLICK
    ]
    
    ACTION_BUTTON_CLICKS = {
        ACTION_LEFT_CLICK: (MouseButton.left, 1),
        ACTION_RIGHT_CLICK: (MouseButton.right, 1)
    }

    def __init__(self,
                 index, 
                 engine: ANEngineInterface):
        '''
        Instanced class to hold sets of hotkeys and ui components.
        '''
        self.index = index
        self._engine = weakref.ref(engine)
        self.mouse_position = None
        self.action = ACTION_LEFT_CLICK
        
        self._init_hotkeys()

    def _init_hotkeys(self):
        '''
        Initialize hotkeys and bind them to their corresponding functions.
        '''
        self.record_hotkey = ANHotKey(self._record_position)
        self.click_hotkey = ANHotKey(self._click_position)
        self.record_hotkey.hotkey = f'ctrl+alt+{self.index + 1}'
        self.click_hotkey.hotkey = f'alt+{self.index + 1}'
        self.record_hotkey.activate()
        self.click_hotkey.activate()

    def _record_position(self):
        self.mouse_position = self.mouse.position
        self.notifier.notify()

    def _click_position(self):
        '''
        Perform the configured action at the recorded mouse position.
        '''
        if self.mouse_position:
            self.mouse.position = self.mouse_position
            button, clicks = ANAnchor.ACTION_BUTTON_CLICKS.get(self.action, (MouseButton.left, 1))
            self.mouse.click(button, clicks)
        
    def _update_record_hotkey(self):
        self.record_hotkey.set_new_hotkey()
        self.notifier.notify()
        
    def _update_click_hotkey(self):
        self.click_hotkey.set_new_hotkey()
        self.notifier.notify()
        
    def update_record_hotkey(self):
        threading.Thread(target=self._update_record_hotkey, daemon=True).start()

    def update_click_hotkey(self):
        threading.Thread(target=self._update_record_hotkey, daemon=True).start()

    def destroy(self, save=True):
        self.record_hotkey.deactivate()
        self.click_hotkey.deactivate()

        if save:
            self.notifier.notify()
    
    def to_dict(self):
        '''
        Converts the anchor instance to a dictionary for serialization.
        '''
        return {
            'index': self.index,
            'record_hotkey': self.record_hotkey.hotkey,
            'click_hotkey': self.click_hotkey.hotkey,
            'mouse_position': self.mouse_position if hasattr(self, 'mouse_position') else None,
            'action': self.action
        }

    @staticmethod
    def from_dict(anchor_dict, engine):
        new_anchor = ANAnchor(anchor_dict['index'], engine)
        new_anchor.record_hotkey.hotkey = anchor_dict['record_hotkey']
        new_anchor.click_hotkey.hotkey = anchor_dict['click_hotkey']
        new_anchor.action = anchor_dict['action']

        if anchor_dict['mouse_position']:
            new_anchor.mouse_position = anchor_dict['mouse_position']
        else:
            new_anchor.mouse_position = None

        return new_anchor
    
    @property
    def mouse(self):
        return self._engine().get_mouse()

    @property
    def notifier(self):
        return self._engine().get_notifier()