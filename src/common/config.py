
from pynput.mouse import Button as MouseButton


SCREEN_WIDTH = 400
SCREEN_HEIGHT = 700

UI_SCALE = 0.8

TASKBAR_ICON_PATH = 'src/ui/custom/icons/anchor.ico'

MAX_ANCHORS = 5

TITLE_STR = 'Anchor'

ACTION_LEFT_CLICK = "left click"
ACTION_RIGHT_CLICK = "right click"

ACTIONS = (ACTION_LEFT_CLICK, ACTION_RIGHT_CLICK)

ACTION_BUTTON_CLICKS = {
        ACTION_LEFT_CLICK: (MouseButton.left, 1),
        ACTION_RIGHT_CLICK: (MouseButton.right, 1)
}
