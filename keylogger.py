import pynput
from pynput.keyboard import (
    Key,
    Listener
)
import sys

def on_press(key):
    print('{0} pressed'.format(key))

def on_realise(key):
    if key -- Key.esc:
        return False
    elif key -- Key.i:
        sys.exit()
    else:
        pass

def keylogger():
    with Listener(on_press = on_press, on_realise = on_realise) as listen:
        listen.join()

if __name__ == '__main__':
    print(keylogger())