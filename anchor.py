import keyboard
import time
from tkinter import Tk, Label, Entry, Button as TkButton, StringVar, ttk
from pynput.mouse import Button as MouseButton, Controller as MouseController

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
            time.sleep(0.1)  # waits for 100ms
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

root = Tk()
root.title("Anchor")
root.geometry('350x450')  # width x height

hotkey_record_entry = [StringVar(value=f'ctrl+alt+{i+1}') for i in range(5)]
hotkey_click_entry = [StringVar(value=f'alt+{i+1}') for i in range(5)]

for i in range(5):
    Label(root, text=f"Record position {i+1}:").grid(row=i*3, column=0)
    record_position_entry = Entry(root, textvariable=hotkey_record_entry[i])
    record_position_entry.grid(row=i*3, column=1)
    TkButton(root, text="Set hotkey", command=lambda i=i: start_capturing(hotkey_record_entry[i])).grid(row=i*3, column=2)

    Label(root, text=f"Action hotkey {i+1}:").grid(row=i*3+1, column=0)
    click_position_entry = Entry(root, textvariable=hotkey_click_entry[i])
    click_position_entry.grid(row=i*3+1, column=1)
    TkButton(root, text="Set hotkey", command=lambda i=i: start_capturing(hotkey_click_entry[i])).grid(row=i*3+1, column=2)

    Label(root, text=f"Action {i+1}:").grid(row=i*3+2, column=0)
    action_combobox = ttk.Combobox(root, values=["left click", "right click", "double left click"])
    action_combobox.current(0)
    actions[i] = action_combobox
    action_combobox.grid(row=i*3+2, column=1)

TkButton(root, text="Activate all hotkeys", command=lambda: [set_hotkey(i) for i in range(5)]).grid(row=15, column=1)

root.mainloop()
