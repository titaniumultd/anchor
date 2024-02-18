
from abc import ABC, abstractmethod


class ANProfileControllerInterface(ABC):
    """
    Interface declaration for the profle controller.
    """

    @abstractmethod
    def load_profiles(self) -> None:
        pass

    @abstractmethod
    def get_current_profile(self) -> str:
        pass

    @abstractmethod
    def has_profiles(self) -> bool:
        pass

    @abstractmethod
    def get_profile_names(self) -> list:
        pass

    @abstractmethod
    def get_profiles(self) -> dict:
        pass

    @abstractmethod
    def update_profile(self, name: str, data) -> None:
        pass