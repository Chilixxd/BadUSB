# How did you come in here?
# Plz no touch my code and i'll be happy :-)
import time
from pynput.keyboard import Key, Controller
keyboard = Controller()

time.sleep(1)

keyboard.press(Key.cmd)
keyboard.press(Key.cmd)
keyboard.press('r')
time.sleep(1)
keyboard.release('r')
keyboard.release(Key.cmd)
keyboard.release(Key.cmd)
time.sleep(1)

keyboard.type('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
time.sleep(1)
keyboard.press(Key.enter)
time.sleep(1)
keyboard.release(Key.enter)
