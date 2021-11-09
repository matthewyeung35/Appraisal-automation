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

#for page 4 interior table, enter room count if room exists
def table_enter(room):
    if int(room)>0:
        keyboard.type(str(room))

def main():
    global keyboard
    interior_finishes = None
    if interior_finishes != None:
        if '1' in interior_finishes:
            print ('tick')
    #-----------
    #if dont want auto fill table, use: tab(85)
    # at cost approach table, garage
    #['separate entrance', '0', 'living room', '0', 'dining room', '0', 'kitchen', '0', 'recreational room', '1', 'family room', '0', 'den', '0', 'laundry room', '1', 'storage room', '1', 'bedroom', '0', 'full bathroom', '1', '2-piece bathroom', '0']
if __name__ == "__main__":
    main()

