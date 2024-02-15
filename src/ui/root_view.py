
from src.ui.anchor.anchor_settings import ANAnchorSettings
from src.ui.view import ANView


class ANRootView(ANView):
    """
    Root view potentially containing multiple different top level views (ie. login or main anchor view).
    """

    def load_frames(self):
        self.place(x=0, y=0, relwidth=1, relheight=1)

        # tk.Label(self, background="red").place(x=0, y=0, relwidth=1, relheight=1)

        self.anchor_settings = ANAnchorSettings(self, self.get_engine())
        self.anchor_settings.pack(expand=True, fill='both', padx=10, pady=10)