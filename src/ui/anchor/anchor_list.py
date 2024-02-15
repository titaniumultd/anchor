
from src.ui.anchor.anchor_frame import ANAnchorView
from src.ui.custom.frame import ANFrame

class ANAnchorList(ANFrame):
    """
    View containing list of anchor views, editable by the user.
    """

    def load_subviews(self):
        self.grid_columnconfigure(0, weight=1)

        for anchor in self.get_engine().get_anchors_controller().get_anchors():
            anchor_view = ANAnchorView(self, self.get_engine(), anchor)
            anchor_view.grid(column=0, sticky='news', pady=10)
