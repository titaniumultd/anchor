
import customtkinter as ctk

from src.ui.custom.frame import ANFrame
from src.common.config import ACTIONS, UI_SCALE

X_PADDING = 4
Y_PADDING = 4


class ANAnchorView(ANFrame):
    """
    View contaiing anchor details and buttons.
    """

    def __init__(self, 
                 master,  
                 anchor):
        self._anchor = anchor

        self._click_hotkey = ctk.StringVar(value=anchor.click_hotkey.hotkey)
        self._record_hotkey = ctk.StringVar(value=anchor.record_hotkey.hotkey)

        super().__init__(master)

    def load_subviews(self):
        self._scale_ui(UI_SCALE)
        self._init_subviews()
        self._layout_subviews()
        self._set_subview_content()
        self._add_tracing()

    def _init_subviews(self):
        self.columnconfigure((0, 1, 2), weight=1)
        self.rowconfigure((0, 1, 2), weight=1)

        self.record_position_label = ctk.CTkLabel(self)
        self.record_position_entry = ctk.CTkEntry(self)
        self.record_position_button = ctk.CTkButton(self, text="Set", command=self._update_record_hotkey)

        self.click_position_label = ctk.CTkLabel(self)
        self.click_position_entry = ctk.CTkEntry(self)
        self.click_position_button = ctk.CTkButton(self, text="Set", command=self._update_click_hotkey)

        self.action_label = ctk.CTkLabel(self)
        self.action_combobox = ctk.CTkComboBox(self, values=ACTIONS, command=self._update_action)

    def _layout_subviews(self):
        self.record_position_label.grid(row=0, column=0, pady=Y_PADDING, sticky='e')
        self.record_position_entry.grid(row=0, column=1, padx=X_PADDING, pady=Y_PADDING, sticky='news')
        self.record_position_button.grid(row=0, column=2, sticky='w')

        self.click_position_label.grid(row=1, column=0, pady=Y_PADDING, sticky='e')
        self.click_position_entry.grid(row=1, column=1, padx=X_PADDING, pady=Y_PADDING, sticky='news')
        self.click_position_button.grid(row=1, column=2, sticky='w')

        self.action_label.grid(row=2, column=0, pady=Y_PADDING, sticky='e')
        self.action_combobox.grid(row=2, column=1, padx=X_PADDING, pady=Y_PADDING, sticky='news')

    def _set_subview_content(self):
        self.record_position_label.configure(text=f"Drop Anchor {self.index + 1}:")
        self.record_position_entry.configure(textvariable=self._record_hotkey)

        self.click_position_label.configure(text=f"Hotkey {self.index + 1}:")
        self.click_position_entry.configure(textvariable=self._click_hotkey)

        self.action_label.configure(text=f"Action {self.index + 1}:")
        self.action_combobox.set(self._anchor.action)

    def _scale_ui(self, scalar:float):
        ctk.set_window_scaling(scalar)
        ctk.set_widget_scaling(scalar)

    def _add_tracing(self):
        """
        Adds variable tracing for entry fields so we can persist any manual changes the user makes.
        """
        self._record_hotkey.trace_add('write', self._record_entry_did_update)
        self._click_hotkey.trace_add('write', self._click_entry_did_update)

    @property
    def index(self):
        return self._anchor.index

    def _update_record_hotkey(self):
        self._anchor.update_record_hotkey()
        self._record_hotkey.set(self._anchor.record_hotkey.hotkey)

    def _update_click_hotkey(self):
        self._anchor.update_click_hotkey()
        self._click_hotkey.set(self._anchor.click_hotkey.hotkey)

    def _update_action(self, action):
        self._anchor.update_action(self.action_combobox.get())

    # Tracing Callbacks

    def _record_entry_did_update(self, *args):
        if len(self._record_hotkey.get()) > 0 and self._record_hotkey.get()[-1] != '+':
            self._anchor.record_hotkey.hotkey = self._record_hotkey.get()
            #self._engine().get_notifier().notify() Todo: connect to viewmodel

    def _click_entry_did_update(self, *args):
        if len(self._click_hotkey.get()) > 0 and self._click_hotkey.get()[-1] != '+':
            self._anchor.click_hotkey.hotkey = self._click_hotkey.get()
            #self._engine().get_notifier().notify()