
from src.common.anchor_model import ANAnchorModelInterface
from src.common.interfaces.engine_interface import ANEngineInterface

from src.ui.anchor.anchor_view import ANAnchorView
from src.ui.custom.frame import ANFrame


class ANAnchorList(ANFrame):
    """
    View containing list of anchor views, editable by the user.
    """
    def __init__(self, 
                master: ANFrame, 
                engine: ANEngineInterface
                ):
        
        self._anchor_controller = engine.get_anchor_controller()
        super().__init__(master)

    def _load_subviews(self):
        self.grid_columnconfigure(0, weight=1)
        anchors = self._get_anchor_list()

        for anchor in anchors:
            anchor_view = ANAnchorView(self, anchor, self._anchor_controller)
            anchor_view.grid(column=0, sticky='news', pady=10)


    def _get_anchor_list(self) -> list[ANAnchorModelInterface]:
        return self._anchor_controller.get_anchors()