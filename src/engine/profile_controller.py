
import logging
import weakref

from src.common.interfaces.engine_interface import ANEngineInterface
from src.common.interfaces.profile_interface import ANProfileControllerInterface
from src.common.interfaces.state_interface import ANStateControllerInterface

class ANProfileController(ANProfileControllerInterface, object):
    """
    Manages the user's set profiles.
    """
    def __init__(self, engine: ANEngineInterface):
        self._engine = weakref.ref(engine)

        self._current_profile = 'default'
        self._profiles = {}
        self._last_profile = None

    # Public Methods

    def load_profiles(self) -> None:
        # self.profiles_combobox['values'] = list(state['profiles'].keys())
        # self.profiles_combobox.set(state['last_profile'])

        state = self._get_state_controller().get_state()

        self._last_profile = state['last_profile']

        if 'profiles' in state:
            self._current_profile = state['last_profile']
            self._profiles = state['profiles']
        else:
            logging.error("Invalid state.json format. Expected a dictionary with 'profiles' key.")

    def has_profiles(self) -> bool:
        return len(self._profiles) > 0

    def get_current_profile(self) -> str:
        return self._current_profile
    
    def get_profile_names(self) -> list:
        return self._profiles.keys()
    
    def get_profiles(self) -> dict:
        return self._profiles

    # Private Methods
            
    def _get_state_controller(self) -> ANStateControllerInterface:
        return self._engine().get_state_controller()