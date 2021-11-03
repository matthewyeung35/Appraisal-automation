from pynput.keyboard import Key, Controller
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

# for page 4 effective age
def effective_age():
    if year_built >= '2019':
        e_age = '1'
    elif year_built >= '2017':
        e_age = '2'
    elif year_built >= '2015':
        e_age = '3'
    elif year_built >= '2006':
        e_age = '5'
    elif year_built >= '1996':
        e_age = '10'
    elif type != '0' or year_built >= '1986':
        e_age = '15'
    else:
        e_age = '20'
    if type == '0':
        remain_life = str(55 - int(e_age))
    else:
        remain_life = str(50 - int(e_age))
    return e_age + 'E', remain_life + '+-' 

# for page 4 all floring comment
def all_flooring_gen():
    total_floor = interior1_floor
    if storey != '1':
        for floor in interior2_floor:
            if floor not in total_floor:
                total_floor.append(floor)
    if storey == '2 1/2' or storey == '3':
        for floor in interior3_floor:
            if floor not in total_floor:
                total_floor.append(floor)
    total_floor.sort(key = int)
    print (total_floor)
    return floor_comment_gen(total_floor).capitalize()


# main function for auto input pdf
def auto_input():
    global keyboard
    keyboard = Controller()
    print ('prepare to move mouse: 3 secs')

    print ()
    # seconds of prepare time
    time.sleep(3)
    # start from page3 - APPRAISER:
    if city == 'Ottawa':
        keyboard.type('Sindu R. Rajaruban')
    else:
        keyboard.type('Ruban Kanagenthiran')
    tab(12)
    enter()
    tab(2)
    enter()
    tab(7)
    if ownership == '0':
        down(2)
    else:
        down(6)
    tab(15)
    # Occupied by:
    if occupy == '0':
        down(2)
    elif occupy == '1':
        down(4)
    elif occupy == '2':
        down(7)
    elif occupy == '3':
        down(3)
    # template skips after Taxes$ to EASEMENTS: Utility/Access/Other
    tab(2)
    #ownership restrictions extra checkbox
    if ownership_restriction_checkbox == '1':
        tab(1)
    enter()
    tab(23)
    if electric == '1':
        right(1)
    tab(2)
    ''' 
    Attach=0/Builtin=1/Detach=2/Underg=3/Aboveg=4/None+Driveway=5/NoneNone=6
    parking_type = '0'
    parking_no = '1'
    '''
    # parking starting at DRIVEWAY: PRIVATE
    if parking_type == '0':
        park_comment = parking_no + ' Attach.'
    elif parking_type == '1':
        park_comment = parking_no + ' Builtin.'
    elif parking_type == '2':
        park_comment = parking_no + ' Detach.'
    elif parking_type == '3':
        park_comment = parking_no + ' Underg.'
    elif parking_type == '4':
        park_comment = parking_no + ' Aboveg.'
    elif parking_type == '5' or parking_type == '6':
        park_comment = 'None'
    if ownership == '0':
        if parking_type == '6':
            enter()
        tab(3)
        if parking_no == '1':
            enter()
            tab(1)
            enter()
            tab(1)
        else:
            tab(2)
        tab(3)
        if parking_type != '6':
            enter()
        tab(6)
        if parking_type == '5' or parking_type == '6':
            enter()
        tab(2)
        if parking_type == '6':
            enter()
        tab(2)
        enter()
        tab(1)
        keyboard.type(park_comment)
    # for condo townhouse template, might have to make changes
    elif ownership == '1' and (type == '2' or type == '4'):
        if parking_type == '6' or parking_type == '3' or parking_type == '4':
            enter()
        tab(1)
        if parking_type == '3' or parking_type == '4':
            enter()
        tab(2)     
        if parking_type == '3' or parking_type == '4':
            enter()
            tab(2)
        elif int(parking_no) > 1:
            enter()
            tab(1)
            enter()
            tab(1)
        else:
            tab(2)
        tab(2)
        if parking_type == '3':
            enter()
        tab(7)
        if parking_type == '4' or parking_type == '5' or parking_type == '6':
            enter()
        tab(2)
        if parking_type == '3' or parking_type == '6':
            enter()
        tab(3)
        keyboard.type(park_comment)
    elif ownership == '1' and type == '3':
        tab(1)
        if parking_type == '6':
            enter()
        tab(6)
        if parking_type == '6':
            enter()   
        tab(1)
        if parking_type == '6':
            enter()
        tab(6)
        if parking_type == '6':
            enter()
        tab(4)
        enter()
        tab(1)
        keyboard.type(park_comment)
    tab(5)
    right(1)
    tab(1)
    right(2)
    tab(2)
    # start at page 4 -CONSTRUCTION COMPLETE:
    time.sleep(10)
    enter()
    enter()
    tab(2)
    keyboard.type(year_built)
    tab(1)
    e_age, remain_life = effective_age()
    keyboard.type(e_age) 
    tab(1)
    keyboard.type(remain_life)
    tab(1)
    right(1)
    tab(1)
    keyboard.type(sqft)
    tab(4)
    enter()
    tab(3)
    # start from PROPERTY TYPE:
    if ownership == '0':
        down(2)
        tab(1)
        if type == '0':
            down(2)
        elif type == '1':
            down(3)
        elif type == '2':
            down(4)
        tab(1)
        if storey == '1':
            down(2)
        elif storey == '1 1/2':
            down(4)
        elif storey == '2':
            down(6)
        elif storey == ' 2 1/2':
            down(7)
        elif storey == '3':
            down(8)
        tab(2)
        if basement == '3':
            down(6)
        else:
            down(2)
        tab(1)
        if basement == '0':
            down(3)
        elif basement == '1':
            down(4)
        elif basement == '2':
            down(5)
        tab(4)
        # stops at CONDITION bug
        time.sleep(6)
        tab(1)
        # at exterior finish: brick=0/stone=1/vinyl=2/concrete=3/stucco=4 (a list)
        if exterior_finish == ['0']:
            down(2)
        elif exterior_finish == ['0', '2']:
            down(4)
        elif exterior_finish == ['2']:
            down(13)
        tab(3)
        right(1)
        tab(1)
        right(1)
        tab(1)
        keyboard.type('1')
        tab(1)
        keyboard.type(str(int(total_bed)-1))
        tab(6)
        keyboard.type(total_partial)
        tab(2)
        keyboard.type(total_bath)
        tab(19)
        i_f = interior_finishes.split(',')
        if i_f[0] == '1':
            enter()
        tab(2)
        if i_f[1] == '1':
            enter()
        tab(1)
        # starts at FLOORING

def assign_var():
    global city, district, ownership, type, condo_location, occupy, adverse, facilities, townhouse_location, adverse_range, nuclear_station, street_type
    global storey, electric, parking_type, parking_no, lease, basement, freehold_location, total_bed, total_partial, total_bath, interior_finishes
    global basement_comments, interior_comments, sales_history_comments, site_neighbourhood_comments, year_built, sqft, exterior_finish, ownership_restriction_checkbox, interior1_floor, interior2_floor, interior3_floor
    city = 'Ottawa'
    district = 'Markville'
    # Free=0/condo=1
    ownership = '0'
    # Det=0/Semi=1/Town=2/Apt=3/Stack=4
    type = '0'
    storey = '2'
    # lot shape, interior/end/corner, backing
    freehold_location = 'rectangular,interior,other residential lots'
    # townhouse location
    townhouse_location = 'end'
    # Commercial=0/Residential=1/Main=2/Commuter=3 front street
    street_type = '1'
    # occupy Owner=0/Tenant=1/Both=2/vacant=3
    occupy = '0'
    # Attach=0/Builtin=1/Detach=2/Underg=3/Aboveg=4/None+Driveway=5/NoneNone=6
    parking_type = '3'
    parking_no = '1'
    # finished=0/partly=1/unfin=2/none=3
    basement = '0'
    adverse = ''
    electric = '1'
    total_bed = '3'
    total_partial = '1' 
    total_bath = '2'
    # potlight/crown moulding
    interior_finishes = '1,1'
    # brick=0/stone=1/vinyl=2/concrete=3/stucco=4 (a list)
    exterior_finish = ['0', '2']
    basement_comments = 'dummy for basement comment'
    interior_comments = 'dummy for interior comment'
    sales_history_comments = 'dummy for sales history'
    site_neighbourhood_comments = 'dummy for site&neighbourhood'
    year_built = '2001'
    sqft = '1500'
    interior1_floor, interior2_floor, interior3_floor = ['2','3'], ['1'], ['3']
    ownership_restriction_checkbox = '1'

def floor_comment_gen(flooring):
    result = ('')
    floor_type_count = 0
    floor_type_total = len(flooring)
    for i in flooring:
        if i == '0':
            result += ('hardwood')
        elif i == '2':
            result += ('laminate')
        elif i == '1':
            result += ('broadloom')
        elif i == '3':
            result += ('ceramic tiles')
        if floor_type_count < (floor_type_total-2):
            result += (', ')
        elif floor_type_count == (floor_type_total-2):
            result += (', and ')
        floor_type_count += 1
    return result

def main():
    global keyboard
    keyboard = Controller()
    assign_var()
    auto_input()
    print (all_flooring_gen())

    print ('Done')
if __name__ == "__main__":
    main()

