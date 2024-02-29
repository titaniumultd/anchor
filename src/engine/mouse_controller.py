
from pynput import mouse


class ANMouseController(object):
    def __init__(self):
        self._controller = mouse.Controller()

    def get_position(self) -> tuple[int, int]:
        return self._controller.position
    
    def set_position(self, position: tuple[int, int]):
        self._controller.position = position

    def click(self, laterality:str):
        button = mouse.Button.left if laterality=='left click' else mouse.Button.right
        self._controller.click(button=button)