
from src.ui.config.config_view import ANAnchorSettings
from src.ui.custom.frame import ANFrame


class ANRootView(ANFrame):
    """
    Root view potentially containing multiple different top level views (ie. login or main anchor view).
    """

    def load_subviews(self):
        self.place(x=0, y=0, relwidth=1, relheight=1)

        # tk.Label(self, background="red").place(x=0, y=0, relwidth=1, relheight=1)

        self.anchor_settings = ANAnchorSettings(self.get_root(), self.get_view())
        self.anchor_settings.pack(expand=True, fill='both', padx=10, pady=10)