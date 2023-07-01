"""
This script is now retired and retained only for reference
"""


import time
import tkinter
from tkinter import ttk

import keyboard
from pynput.mouse import Button as MouseButton
from pynput.mouse import Controller as MouseController

ANCHOR_ROWS = 4
MAX_ANCHORS = 5
UI_ELEMENT_PAD_X = 3
UI_ELEMENT_PAD_Y = 2
UI_FRAME_PAD_X = 0

mouse = MouseController()

captured_keys = []
active_var = None

positions = [None]*5
actions = [None]*5

def on_key_press(e):
    global captured_keys
    captured_keys.append(e.name)
    return False  # allow key events to pass to other handlers

def on_key_release(e):
    global captured_keys, active_var
    if active_var is not None:
        active_var.set('+'.join(captured_keys))
        stop_capturing(e)
    return False 

def set_hotkey(index):
    def record_position(e=None):
        global positions
        positions[index] = mouse.position

    def click_position(e=None):
        global actions
        if positions[index] is not None:
            mouse.position = positions[index]
            time.sleep(0.1)  # waits for 100ms to avoid clicking before adjusting cursor on some system
            action = actions[index].get()
            if action == "left click":
                mouse.click(MouseButton.left)
            elif action == "right click":
                mouse.click(MouseButton.right)
            elif action == "double left click":
                mouse.click(MouseButton.left, 2)

    hotkey_record = hotkey_record_entry[index].get()
    hotkey_click = hotkey_click_entry[index].get()

    keyboard.add_hotkey(hotkey_record, record_position)
    keyboard.add_hotkey(hotkey_click, click_position)

def start_capturing(var):
    global active_var
    active_var = var
    keyboard.hook_key('esc', stop_capturing, suppress=True)
    keyboard.on_press(on_key_press, suppress=True)
    keyboard.on_release(on_key_release, suppress=True)

def stop_capturing(e):
    global active_var, captured_keys
    keyboard.unhook_all()
    active_var = None
    captured_keys = []
    return False

root = tkinter.Tk()
root.title("Anchor")
root.grid_columnconfigure(0, weight=1)  # adjust size with window
root.grid_rowconfigure(0, weight=1)

hotkey_record_entry = [tkinter.StringVar(value=f'ctrl+alt+{i+1}') for i in range(5)]
hotkey_click_entry = [tkinter.StringVar(value=f'alt+{i+1}') for i in range(5)]

anchors = {}
def drop_an_anchor():
    i = len(anchors)
    print(i)
    if i >= 5: return  # maximum of 5 anchors

    record_position_label = tkinter.Label(root, text=f"Drop Anchor {i+1}:")
    record_position_label.grid(row=i*ANCHOR_ROWS, column=0, pady=UI_ELEMENT_PAD_Y)
    record_position_entry = tkinter.Entry(root, textvariable=hotkey_record_entry[i])
    record_position_entry.grid(row=i*ANCHOR_ROWS, column=1)
    record_position_button = tkinter.Button(root, text="Set", command=lambda i=i: start_capturing(hotkey_record_entry[i]))
    record_position_button.grid(row=i*ANCHOR_ROWS, column=2)

    click_position_label = tkinter.Label(root, text=f"Hotkey {i+1}:")
    click_position_label.grid(row=i*ANCHOR_ROWS+1, column=0, pady=UI_ELEMENT_PAD_Y)
    click_position_entry = tkinter.Entry(root, textvariable=hotkey_click_entry[i])
    click_position_entry.grid(row=i*ANCHOR_ROWS+1, column=1)
    click_position_button = tkinter.Button(root, text="Set", command=lambda i=i: start_capturing(hotkey_click_entry[i]))
    click_position_button.grid(row=i*ANCHOR_ROWS+1, column=2)

    action_label = tkinter.Label(root, text=f"Action {i+1}:")
    action_label.grid(row=i*ANCHOR_ROWS+2, column=0, pady=UI_ELEMENT_PAD_Y)
    action_combobox = ttk.Combobox(root, values=["left click", "right click", "double left click"])
    action_combobox.current(0)
    actions[i] = action_combobox
    action_combobox.grid(row=i*ANCHOR_ROWS+2, column=1)

    remove_anchor_button = tkinter.Button(root, text="Delete", command=lambda i=i: remove_anchor(i))
    remove_anchor_button.grid(row=i*ANCHOR_ROWS+2, column=2, padx=UI_ELEMENT_PAD_X)

    separator = tkinter.Label(root, text="")
    separator.grid(row=i*ANCHOR_ROWS+3, column=0, pady=UI_FRAME_PAD_X)  # Add vertical padding between anchors

    anchor_ui_elements = [
        record_position_label, record_position_entry, record_position_button,
        click_position_label, click_position_entry, click_position_button,
        action_label, action_combobox, remove_anchor_button, separator
    ]

    anchors[i] = anchor_ui_elements

def remove_anchor(index):
    # Remove UI elements from window
    for widget in anchors[index]:
        widget.grid_forget()
    # Remove hotkeys with error handling for keys not yet set
    try:
        keyboard.remove_hotkey(hotkey_record_entry[index].get())
    except KeyError:
        pass
    try:
        keyboard.remove_hotkey(hotkey_click_entry[index].get())
    except KeyError:
        pass 
    # Shift down the anchors above the removed one
    for i in range(index+1, len(anchors)):
        for widget in anchors[i]:
            widget.grid(row=widget.grid_info()["row"] - ANCHOR_ROWS)
        # Update labels for the shifted anchor
        anchors[i][0]['text'] = f"Drop Anchor {i}:"
        anchors[i][3]['text'] = f"Hotkey {i}:"
        anchors[i][6]['text'] = f"Action {i}:"
        anchors[i-1] = anchors[i]

    del anchors[len(anchors)-1]

drop_an_anchor()
tkinter.Button(root, text="New Anchor", command=drop_an_anchor).grid(row=ANCHOR_ROWS*MAX_ANCHORS, column=0)
tkinter.Button(root, text="Activate hotkeys", command=lambda: [set_hotkey(i) for i in range(5)]).grid(row=ANCHOR_ROWS*MAX_ANCHORS, column=1)

root.mainloop()