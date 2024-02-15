
import logging
import weakref

from src.common.anchor import ANAnchor
from src.common.config import MAX_ANCHORS
from src.common.interfaces.engine_interface import ANEngineInterface
from src.common.interfaces.anchors_interface import ANAnchorsControllerInterface
from src.common.interfaces.profile_interface import ANProfileControllerInterface
from src.common.interfaces.state_interface import ANStateControllerInterface


class ANAnchorsController(ANAnchorsControllerInterface, object):
    """
    Manages anchors. To-Do: Separate Anchors from UI
    """

    def __init__(self, 
                 engine: ANEngineInterface):
        self._engine = weakref.ref(engine)
        self._anchors = [ANAnchor]

    # Public Methods

    def load_anchors(self) -> list:
        profile_controller = self._get_profile_controller()

        if profile_controller.has_profiles():
            current_profile = profile_controller.get_current_profile()
            raw_anchors = self._get_profile_anchors(current_profile)
            for anchor_dict in raw_anchors:
                new_anchor = ANAnchor.from_dict(anchor_dict, self._engine())
                self._anchors.append(new_anchor)

        while len(self._anchors) < MAX_ANCHORS:
            self._drop_an_anchor()

    def get_anchors(self) -> list:
        return self._anchors
    
    def save_anchors(self) -> None:
        profile_controller = self._get_profile_controller()

        if profile_controller.has_profiles():
            current_profile = profile_controller.get_current_profile()
            profile_controller.update_profile(current_profile, [anchor.to_dict() for anchor in self._anchors])

    def activate_hotkeys(self) -> None:
        for anchor in self._anchors:
            anchor.record_hotkey.activate()
            anchor.click_hotkey.activate()

    def deactivate_hotkeys(self) -> None:
        for anchor in self._anchors:
            anchor.record_hotkey.deactivate()
            anchor.click_hotkey.deactivate()
    
    # Private Methods

    def _get_root(self):
        return self._engine().get_root()
    
    def _get_mouse(self):
        return self._engine().get_mouse()
    
    def _get_notifier(self):
        return self._engine().get_notifier()

    def _get_state_controller(self) -> ANStateControllerInterface:
        return self._engine().get_state_controller()

    def _get_profile_controller(self) -> ANProfileControllerInterface:
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
    
    def _drop_an_anchor(self):
        # to-do: clean-up
        if len(self._anchors) >= MAX_ANCHORS:
            return
        
        new_anchor = ANAnchor(len(self._anchors), self._engine())
        self._anchors.append(new_anchor)
        self.save_anchors()
    
    def get_hotkeys_enabled_state(self):
        i = 0
        for anchor in self._anchors:
            if anchor.hotkeys_enabled:
                i += 1
        if len(self._anchors) == i:
            return True
        else:
            return False
    