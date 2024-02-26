
import customtkinter as ctk

from src.common.interfaces.engine_interface import ANEngineInterface
from src.common.interfaces.ui.config_view_model_interface import ANConfigViewModelInterface
from src.common.variables import (SCREEN_HEIGHT, SCREEN_WIDTH,
                                  TASKBAR_ICON_PATH, TITLE_STR)
from src.ui.anchor.anchor_list import ANAnchorList
from src.ui.config.config_view_model import ANConfigViewModel
from src.ui.custom.frame import ANFrame


class ANConfigView(ANFrame):
    def __init__(self, 
                master: ctk.CTk, 
                engine: ANEngineInterface
                ):

        self._master = master
        self._view_model: ANConfigViewModelInterface = ANConfigViewModel(engine)
        
        self._init_window()
        super().__init__(self._master)
        self._load_anchor_subview(engine)

    def _load_subviews(self):
        self.pack()
        self._load_config_subview()

    def _init_window(self):
        self._master.title(TITLE_STR)
        self._master.geometry(f'{SCREEN_WIDTH}x{SCREEN_HEIGHT}')
        self._master.minsize(SCREEN_WIDTH, SCREEN_HEIGHT)
        self._master.iconbitmap(default=TASKBAR_ICON_PATH)
        self._master.protocol("WM_DELETE_WINDOW", self.hide_window)
        
    def _load_anchor_subview(self, engine:ANEngineInterface):
        self._anchor_list = ANAnchorList(self, engine)
        self._anchor_list.grid(column=0, row=0)
    
    def _load_config_subview(self):
        self.activate_hotkeys_button = ctk.CTkCheckBox(master=self,
                                                       text="Activate hotkeys",
                                                       variable=self._view_model.hotkey_var,
                                                       command=self.toggle_global_hotkeys)

        self.activate_hotkeys_button.grid(column=0, row=1)

    def toggle_global_hotkeys(self):
        self._view_model.toggle_global_hotkey_state()

    def show_window(self):
        self._master.deiconify()

    def hide_window(self):
        self._master.withdraw()
    
    def exit_app(self):
        self._master.destroy()