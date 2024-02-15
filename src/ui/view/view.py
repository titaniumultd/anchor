
import customtkinter as ctk
import keyboard

from src.common.interfaces.view_interface import ANViewInterface
from src.common.config import (SCREEN_HEIGHT, SCREEN_WIDTH, TASKBAR_ICON_PATH,
                               TITLE_STR)
from src.ui.view.root_view import ANRootView
from src.ui.view.tray import ANTray


class ANView(ANViewInterface):
    def __init__(self):

        self._root = ctk.CTk()

        self._root.title(TITLE_STR)
        self._root.protocol("WM_DELETE_WINDOW", self.hide_window)
        self._root.geometry(f'{SCREEN_WIDTH}x{SCREEN_HEIGHT}')
        self._root.minsize(SCREEN_WIDTH, SCREEN_HEIGHT)
        self._root.iconbitmap(default=TASKBAR_ICON_PATH)

    def _load_frame(self):
        self._frame = ANRootView(self._root, self)

    def get_root(self) -> ctk.CTk:
        return self._root
    
    def load(self):
        self._load_frame()
        self._tray = ANTray(self)
        self._root.mainloop()
    
    def show_window(self):
        self._root.after(0, self._root.deiconify)
    
    def hide_window(self):
        self._root.after(0, self._root.withdraw)

    def exit(self) -> None:
        keyboard.unhook_all()
        self._root.destroy()
    
    def toggle_hotkeys(self):
        self._view_model().toggle_hotkeys()