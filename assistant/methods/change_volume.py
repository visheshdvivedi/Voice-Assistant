from pynput.keyboard import Key, Controller
import time

def increase_volume():
    keyboard = Controller()
    for i in range(10):
        keyboard.press(Key.media_volume_up)
        keyboard.release(Key.media_volume_up)
        time.sleep(0.1)

def max_volume():
    keyboard = Controller()
    for i in range(50):
        keyboard.press(Key.media_volume_up)
        keyboard.release(Key.media_volume_up)
        time.sleep(0.1)

def mute_volume():
    keyboard = Controller()
    keyboard.press(Key.media_volume_mute)
    keyboard.release(Key.media_volume_mute)

def decrease_volume():
    keyboard = Controller()
    for i in range(10):
        keyboard.press(Key.media_volume_down)
        keyboard.release(Key.media_volume_down)
        time.sleep(0.1)

def main(term):
    if "increase" in term.lower():
        increase_volume()
    elif "decrease" in term.lower():
        decrease_volume()
    elif "max" in term.lower():
        max_volume()
    elif "mute" in term.lower() or "unmute" in term.lower():
        mute_volume()