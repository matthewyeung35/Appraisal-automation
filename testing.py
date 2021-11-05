from pynput.keyboard import Key, Controller
from datetime import datetime
from openpyxl import load_workbook

import time
# delete everything in box
def delete():
    keyboard.press(Key.ctrl)
    keyboard.type('a')
    keyboard.release(Key.ctrl)
    keyboard.press(Key.delete)
    keyboard.release(Key.delete)

# press tab for (times)
def tab(times):
    for _ in range(times):
        keyboard.press(Key.tab)
        keyboard.release(Key.tab)

# press down for (times) - for box type input
def down(times):
    for _ in range(times):
        keyboard.press(Key.down)
        keyboard.release(Key.down)

# press right for (times)
def right(times):
    for _ in range(times):
        keyboard.press(Key.right)
        keyboard.release(Key.right)

# press right for (times)
def left(times):
    for _ in range(times):
        keyboard.press(Key.left)
        keyboard.release(Key.left)

# press enter single time
def enter():
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

def main():
    global keyboard
    keyboard = Controller()
    # at view property 
    time.sleep(3)
    tab(3)
    delete()
    tab(4)
    delete()
    tab(1)
    time.sleep(1)
    tab(7)
    time.sleep(0.5)
    tab(12)
    time.sleep(0.5)
    tab(1)
    time.sleep(0.2)
    tab(1)
    enter()
    tab(1)
    enter()
    tab(2)
    enter()
    tab(1)
    enter()
    tab(2)
    enter()
    tab(8)
    time.sleep(1)
    tab(8)
    time.sleep(1)
    tab(1)
    time.sleep(0.2)
    tab(4)
if __name__ == "__main__":
    main()

