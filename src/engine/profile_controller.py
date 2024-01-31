
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
    
    def update_profile(self, name: str, data) -> None:
        if name is not None and data is not None:
            self._profiles[name] = data
            self._get_state_controller().update_state("profiles", self._profiles)

    # Private Methods
            
    def _get_state_controller(self) -> ANStateControllerInterface:
        return self._engine().get_state_controller()
    

    # TODO
    # def get_profiles(self):
    #     state = self.read_state_file()
    #     return state.get('profiles', {})

    # def add_profile(self, profile_name):
    #     state = self.read_state_file()
    #     state['profiles'][profile_name] = []
    #     state['last_profile'] = profile_name
    #     self.write_state_file(state)

    # def create_new_profile(self):
    #     new_profile_name = f"profile{len(self.profiles_combobox['values']) + 1}"
    #     self.add_profile(new_profile_name)

    #     profiles = self.get_profiles()
    #     self.profiles_combobox['values'] = list(profiles.keys())
    #     self.profiles_combobox.set(new_profile_name)

    # def delete_profile(self):
    #     selected_profile = self.profiles_combobox.get()
    #     if selected_profile == 'default':
    #         return

    #     state = self.read_state_file()
    #     del state['profiles'][selected_profile]
    #     self.write_state_file(state)

    #     self.profiles_combobox['values'] = list(state['profiles'].keys())
    #     self.profiles_combobox.set('default')
    #     self.switch_profile()

    # def switch_profile(self, event=None):
    #     selected_profile = self.profiles_combobox.get()

    #     if selected_profile == self.current_profile:
    #         return

    #     for anchor in self.anchors:
    #         anchor.destroy(save=False)
    #     self.anchors.clear()

    #     state = self.read_state_file()
    #     if 'profiles' in state:
    #         profiles = state['profiles']
    #         if selected_profile in profiles:
    #             self.current_profile = selected_profile
    #             state['last_profile'] = selected_profile
    #             anchors = profiles[selected_profile]

    #             for anchor_dict in anchors:
    #                 new_anchor = ANAnchor.from_dict(anchor_dict, self.root, self.mouse, self.notifier)
    #                 self.anchors.append(new_anchor)

    #             self.write_state_file(state)
    #         else:
    #             logging.error(f"No such profile: {selected_profile}")
    #     else:
    #         logging.error("Invalid state.json format in switch_profile. Expected a dictionary with 'profiles' key.")