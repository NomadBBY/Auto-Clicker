import threading
import time

from pynput.keyboard import KeyCode, Listener
from pynput.mouse import Button, Controller

delay = 1
button = Button.left
start_stop_key = KeyCode(char='a')
stop_key = KeyCode(char='b')
move_key = KeyCode(char='m')
position_key = KeyCode(char='p')  # new key for mouse position

class ClickMouse(threading.Thread):
    def __init__(self, delay, button):
        super(ClickMouse, self).__init__()
        self.delay = delay
        self.button = button
        self.running = False
        self.program_running = True

    def start_clicking(self):
        self.running = True

    def stop_clicking(self):
        self.running = False

    def exit(self):
        self.stop_clicking()
        self.program_running = False

    def run(self):
        while self.program_running:
            while self.running:
                mouse.click(self.button)
                time.sleep(self.delay)
            time.sleep(2.0)

mouse = Controller()
click_thread = ClickMouse(delay, button)
click_thread.start()

def on_press(key):
    if key == start_stop_key:
        if click_thread.running:
            click_thread.stop_clicking()
        else:
            click_thread.start_clicking()
    elif key == stop_key:
        click_thread.exit()
        listener.stop()
    elif key == move_key:
        mouse.position = (1060, 370)
    elif key == position_key:  # new key event to get the mouse position
        print('Mouse position:', mouse.position)

with Listener(on_press=on_press) as listener:
    listener.join()
