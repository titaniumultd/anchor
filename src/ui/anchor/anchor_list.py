
from customtkinter import CTk

from src.common.anchor_model import ANAnchorModelInterface
from src.common.interfaces.controllers.anchor_controller_interface import ANAnchorControllerInterface
from src.common.interfaces.ui.anchor_view_model_interface import ANAnchorViewModelInterface
from src.ui.anchor.anchor_view_model import ANAnchorViewModel
from src.ui.custom.frame import ANFrame


class ANAnchorList(ANFrame):
    """
    View containing list of anchor views, editable by the user.
    """
    def __init__(self, 
                root: CTk, 
                anchor_controller: ANAnchorControllerInterface
                ):
        self._root = root
        self._anchor_controller = anchor_controller

        #self.pack(expand=True, fill='both')

    def load_subviews(self):
        self.grid_columnconfigure(0, weight=1)
        anchors = self._get_anchor_list()

        for anchor in anchors:
            anchor_view_model:ANAnchorViewModelInterface = ANAnchorViewModel(self._root, anchor, self._anchor_controller)

    def _get_anchor_list(self) -> list[ANAnchorModelInterface]:
        return self._anchor_controller.get_anchors()
