
from pynput import mouse


class ANMouseController(object):

    def get_position(self) -> tuple[int, int]:
        return mouse.Controller.position
    
    def set_position(self, position: tuple[int, int]):
        mouse.Controller.position = position

    def click(self, laterality:str):
        button = mouse.Button.left if laterality=='left click' else mouse.Button.right
        mouse.Controller.click(button=button)