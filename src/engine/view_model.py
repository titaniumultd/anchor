import weakref

from src.common.interfaces.engine_interface import ANEngineInterface
from src.common.interfaces.view_interface import ANViewInterface
from src.ui.root_view import ANRootView


class ANViewModel(object):

    def __init__(self, root, engine:ANEngineInterface):
        self._engine = weakref.ref(engine)
        self._root = root

        self.views = {
            'default': ANRootView(self._root, self)
        }

        self._select_view()

    def _set_default_view(self, view:ANViewInterface):
        self.views['default'] = view

    def _add_view(self, view:ANViewInterface, title:str):
        self.views[title] = view
        
    def _select_view(self, view:str='default'):
        self.current_view = self.views.get(view)

    def restore_ui(self):
        self.enable_all_hotkeys()
        self.undither_all_buttons()

    def disable_all_hotkeys(self):
        self._engine().disable_all_hotkeys()
    
    def enable_all_hotkeys(self):
        self._engine().enable_all_hotkeys()
    
    def dither_all_buttons(self):
        self.current_view.dither_all_buttons()
    
    def undither_all_buttons(self):
        self.current_view.undither_all_buttons()
    
    def update_text_entry(self, text_field, value:str):
        self.current_view.update_text_entry(text_field, value)
    
    def set_hotkey(self):
        pass
    