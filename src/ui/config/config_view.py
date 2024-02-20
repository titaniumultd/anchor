
import customtkinter as ctk
import weakref

from src.ui.custom.frame import ANFrame
from src.common.interfaces.ui.config_view_model_interface import ANConfigViewModelInterface
from src.common.interfaces.controllers.anchor_controller_interface import ANAnchorControllerInterface
from src.ui.anchor.anchor_list import ANAnchorList
from src.common.variables import TASKBAR_ICON_PATH, TITLE_STR, SCREEN_HEIGHT, SCREEN_WIDTH


class ANConfigView(ANFrame, object):
    def __init__(self, 
                root: ctk.CTk, 
                view_model: ANConfigViewModelInterface,
                anchor_controller: ANAnchorControllerInterface,
                hotkey_var: ctk.IntVar):
        
        self._root = root
        self._view_model = weakref.ref(view_model)
        self._anchor_controller = anchor_controller
        self._hotkey_var = hotkey_var
        
        self._init_layout()

        super().__init__(self._root)

    def load_subviews(self):
        self._load_anchor_subview()
        self._load_config_subview()

    def _init_layout(self):
        self._root.title(TITLE_STR)
        self._root.geometry(f'{SCREEN_WIDTH}x{SCREEN_HEIGHT}')
        self._root.minsize(SCREEN_WIDTH, SCREEN_HEIGHT)
        self._root.iconbitmap(default=TASKBAR_ICON_PATH)

    def _load_anchor_subview(self):
        self._anchor_list = ANAnchorList(self._root, self._anchor_controller)
    
    def _load_config_subview(self):
        self.activate_hotkeys_button = ctk.CTkCheckBox(self,
                                                       text="Activate hotkeys",
                                                       onvalue=1,
                                                       offvalue=0,
                                                       variable=self._hotkey_var,
                                                       command=self._toggle_global_hotkeys)

        self.activate_hotkeys_button.pack(side='right', anchor=ctk.S, pady=(10, 0))
    
    def _get_view_model(self) -> ANConfigViewModelInterface:
        return self._view_model()

    def _toggle_global_hotkeys(self):
        self._get_view_model().toggle_global_hotkey_state()