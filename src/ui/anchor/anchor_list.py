
from src.common.interfaces.controllers.anchor_controller_interface import ANAnchorControllerInterface

from src.ui.anchor.anchor_view import ANAnchorView
from src.ui.custom.frame import ANFrame


class ANAnchorList(ANFrame):
    """
    View containing list of anchor views, editable by the user.
    """
    def __init__(self, 
                master: ANFrame, 
                anchor_controller: ANAnchorControllerInterface
                ):
        
        self._anchor_controller = anchor_controller
        super().__init__(master)

    def _load_subviews(self):
        self.grid_columnconfigure(0, weight=1)
        anchors = self._anchor_controller.get_anchors()

        for anchor in anchors:
            anchor_view = ANAnchorView(self, anchor, self._anchor_controller)
            anchor_view.grid(column=0, sticky='news', pady=10)