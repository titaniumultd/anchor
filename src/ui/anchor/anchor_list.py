
from src.common.anchor_model import ANAnchor
from src.ui.anchor.anchor_view import ANAnchorView
from src.ui.custom.frame import ANFrame


class ANAnchorList(ANFrame):
    """
    View containing list of anchor views, editable by the user.
    """

    def load_subviews(self):
        self.grid_columnconfigure(0, weight=1)
        anchors = self._get_anchor_list()

        for anchor in anchors:
            anchor_view = ANAnchorView(self.get_root(), anchor, self.get_view())
            anchor_view.grid(column=0, sticky='news', pady=10)

    def _get_anchor_list(self) -> list[ANAnchor]:
        return self._view().get_anchor_list()
