
from abc import ABC, abstractmethod

from src.common.interfaces.frame_interface import ANFrameInterface


class ANViewInterface(ABC):

    @abstractmethod
    def load_frames(self, frames:list[ANFrameInterface]):
        pass