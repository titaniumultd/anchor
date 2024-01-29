
import logging
import weakref

from src.common.anchor import ANAnchor
from src.common.interfaces.engine_interface import ANEngineInterface
from src.common.interfaces.anchors_interface import ANAnchorsControllerInterface
from src.common.interfaces.profile_interface import ANProfileControllerInterface


class ANAnchorsController(ANAnchorsControllerInterface, object):
    """
    Manages anchors. To-Do: Separate Anchors from UI
    """

    def __init__(self, engine: ANEngineInterface):
        self._engine = weakref.ref(engine)
        self._anchors = []

    # Public Methods

    def load_anchors(self) -> list:
        profile_controller = self._get_profile_controller()

        if profile_controller.has_profiles():
            current_profile = profile_controller.get_current_profile()
            raw_anchors = self._get_profile_anchors(current_profile)
            for anchor_dict in raw_anchors:
                print(anchor_dict)
                # new_anchor = ANAnchor.from_dict(anchor_dict, self.root, self.mouse, self.notifier)
                # new_anchor.remove_anchor_button['command'] = lambda anchor=new_anchor: self.remove_anchor(anchor)
                # self._anchors.append(new_anchor)

    def get_anchors(self) -> list:
        return self._anchors
    
    # Private Methods

    def _get_profile_controller(self) -> ANProfileControllerInterface:
        assert self._engine() != None

        return self._engine().get_profile_controller()
    
    def _get_profile_anchors(self, name: str) -> list:
        profile_controller = self._get_profile_controller()

        if profile_controller.has_profiles():
            profiles = profile_controller.get_profiles()

            if name in profiles:
                return profiles[name]
            else:
                logging.error(f"No such profile: {name}")

        return []
