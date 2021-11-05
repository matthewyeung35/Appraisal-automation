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
    keyboard = Controller()
    print('starting')
    time.sleep(3)
    storey = '3'
    basement = '3'
    type = '0'
    interior1 = ['foyer', '1', 'living room', '1', 'dining room', '1', 'kitchen', '1', 'family room', '1', 'den', '0', 'office', '0', 'laundry room', '0', 'master bedroom', '0', 'bedroom', '0', 'full ensuite bathroom', '1', 'full bathroom', '0', '2-piece bathroom', '2'] 
    interior2 = ['living room', '0', 'dining room', '0', 'kitchen', '0', 'loft', '1', 'den', '0', 'office', '0', 'laundry room', '1', 'master bedroom', '1', 'bedroom', '3', 'full ensuite bathroom', '1', 'full bathroom', '1', '2-piece bathroom', '0'] 
    interior3 =['loft', '0', 'den', '0', 'office', '0', 'laundry room', '0', 'master bedroom', '1', 'bedroom', '1', 'full ensuite bathroom', '1', 'full bathroom', '1', '2-piece bathroom', '1']
    all_basement_int = ['separate entrance', '0', 'living room', '0', 'dining room', '0', 'kitchen', '0', 'recreational room', '1', 'family room', '0', 'den', '0', 'laundry room', '1', 'storage room', '1', 'bedroom', '0', 'full bathroom', '1', '2-piece bathroom', '0']
    # at interior table, first level entrance  
    # auto fill interior table?
    tab(1)
    if interior1[3] != '1':
        delete()
        tab(1)
        delete()
        tab(1)
        delete()
        tab(1)
    else:
        tab(3)
    enter()
    #in floor 1bathroom
    tab(1)
    delete()
    table_enter(interior1[25])
    tab(2)
    t_full = int(interior1[21]) + int(interior1[23])
    table_enter(t_full)
    enter()
    tab(1)
    t_bed = int(interior1[17]) + int(interior1[19])
    table_enter(t_bed)
    tab(1)
    delete()
    table_enter(interior1[9])
    tab(1)
    delete()
    if interior1[15] == '1':
        keyboard.type('x')
    tab(13)
    # at 2nd F living
    if storey == '1' and type != '3':
        tab(42)
    else:
        if interior2[1] == '1':
            keyboard.type('1')
            tab(1)
            keyboard.type('1')
            tab(1)
            keyboard.type('1')
            tab(1)
        else:
            tab(3)
        enter()
        tab(1)
        table_enter(interior2[23])
        tab(2)
        t_full = int(interior2[19]) + int(interior2[21])
        table_enter(t_full)
        enter()
        tab(1)
        delete()
        t_bed = int(interior2[15]) + int(interior2[17])
        table_enter(t_bed)
        tab(2)
        if interior2[13] == '1':
            keyboard.type('x')
        tab(8)
        # at third floor living
        if storey == '2 1/2' or storey == '3':
            tab(3)
            enter()
            tab(1)
            table_enter(interior3[17])
            tab(2)
            t_full = int(interior3[13]) + int(interior3[15])
            table_enter(t_full)
            enter()
            tab(1)
            t_bed = int(interior3[9]) + int(interior3[11])
            table_enter(t_bed)
            tab(2)
            if interior3[7] == '1':
                keyboard.type('x')
            tab(22)
        else:
            tab(28)
    #at basement entrance
    if basement != '3' and type != '3':
        if all_basement_int[1] == '1':
            keyboard.type('x')
        tab(1)
        table_enter(all_basement_int[3])
        tab(1)
        table_enter(all_basement_int[5])
        tab(1)
        table_enter(all_basement_int[7])
        tab(1)
        enter()
        tab(1)
        table_enter(all_basement_int[23])
        tab(2)
        table_enter(all_basement_int[21])
        enter()
        tab(1)
        table_enter(all_basement_int[19])
        tab(1)
        table_enter(all_basement_int[11])
        tab(1)
        if all_basement_int[15] == '1':
            keyboard.type('x')
        tab(3)
        table_enter(all_basement_int[9])
        tab(13)
    else:
        tab(23)
    time.sleep(5)
    #-----------
    #if dont want auto fill table, use: tab(85)
    # at cost approach table, garage
    #['separate entrance', '0', 'living room', '0', 'dining room', '0', 'kitchen', '0', 'recreational room', '1', 'family room', '0', 'den', '0', 'laundry room', '1', 'storage room', '1', 'bedroom', '0', 'full bathroom', '1', '2-piece bathroom', '0']
if __name__ == "__main__":
    main()

