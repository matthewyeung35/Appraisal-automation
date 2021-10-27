def interior_info():
    global interior1, interior2, interior3
    result = ('')
    while True:
        try:
            print ('sqft?')
            #sqft = input()
            print ('brick=0/stone=1/vinyl=2/concrete=3/stucco=4')
            exterior_finish = input().split(',')
            #for 1 storey
            interior1 = ['foyer', '1']
            print('first floor:')
            print ('living+dining+kitchen? (0 or 1)')
            storey_rooms = input()
            if storey_rooms == '1':
                interior1.extend(['living', '1', 'dining', '1', 'kitchen', '1'])
            print ('family room/den/office/laundry')
            storey_rooms = input().split(',')
            interior1.extend(['family room', storey_rooms[0] , 'den' , storey_rooms[1] , 'office' , storey_rooms[2] , 'laundry room' , storey_rooms[3]])
            print ('master bed/ average bed')
            storey_rooms = input().split(',')
            interior1.extend(['master bedroom', storey_rooms[0] , 'average sized bedroom' , storey_rooms[1]])
            print('ensuite/full/partial bathroom')
            storey_rooms = input().split(',')
            interior1.extend(['full ensuite bathroom', storey_rooms[0] , 'full bathroom' , storey_rooms[1], '2-piece bathroom', storey_rooms[2]])
            print ('hardwood=0/broadloom=1/ceramic=2/laminate=3')
            interior1_floor = input().split(',')
            # for 2 storey
            if storey != '1':
                interior2 = []
                print('second floor:')
                print ('living+dining+kitchen? (0 or 1)')
                storey_rooms = input()
                if input == '1':
                    interior2.extend(['living', '1', 'dining', '1', 'kitchen', '1'])
                print ('loft/den/office/laundry')
                storey_rooms = input().split(',')
                interior2.extend(['loft', storey_rooms[0] , 'den' , storey_rooms[1] , 'office' , storey_rooms[2] , 'laundry room' , storey_rooms[3]])
                print ('master bed/ average bed')
                storey_rooms = input().split(',')
                interior2.extend(['master bedroom', storey_rooms[0] , 'average sized bedroom' , storey_rooms[1]])
                print('ensuite/full/partial bathroom')
                storey_rooms = input().split(',')
                interior2.extend(['full ensuite bathroom', storey_rooms[0] , 'full bathroom' , storey_rooms[1], '2-piece bathroom', storey_rooms[2]])
                print ('hardwood=0/broadloom=1/ceramic=2/laminate=3')
                interior2_floor = input().split(',')
            if storey == '2 1/2 ' or storey == '3':
                interior3=[]
                print('third floor:')
                print ('loft/den/office/laundry')
                storey_rooms = input().split(',')
                interior3.extend(['loft', storey_rooms[0] , 'den' , storey_rooms[1] , 'office' , storey_rooms[2] , 'laundry room' , storey_rooms[3]])
                print ('master bed/ average bed')
                storey_rooms = input().split(',')
                interior3.extend(['master bedroom', storey_rooms[0] , 'average sized bedroom' , storey_rooms[1]])
                print('ensuite/full/partial bathroom')
                storey_rooms = input().split(',')
                interior3.extend(['full ensuite bathroom', storey_rooms[0] , 'full bathroom' , storey_rooms[1], '2-piece bathroom', storey_rooms[2]])
                print ('hardwood=0/broadloom=1/ceramic=3/laminate=4')
                interior3_floor = input().split(',')
        except IndexError:
            print ('Invalid input')
        else:
            break

    # TODO interior finishes
    #print ('Interior finishes?')
    #interior_finishes = input().split(',')

    #interior comment freehold
    # turn house type Det=0/Semi=1/Town=2 to names
    if type == '0':
        house_name = 'detached'
    elif type == '1':
        house_name = 'semi-detached'
    elif type == '2':
        house_name = 'townhouse'
    if ownership == '0':
        result += ('The subject is a {} storey {} dwelling containing approximately {} square feet of living space and is assumed to be in average physical condition at time of inspection. The exterior of the home is finished with mostly {}. '
        'The main floor, finished with {} flooring consists of {}'.format(storey, house_name, sqft, exterior_comment_gen(exterior_finish), floor_comment_gen(interior1_floor), interior_room_gen(interior1)))
        if storey != '1':
            result += ('The second floor, finished with {} flooring, consists of {}'.format(floor_comment_gen(interior2_floor), interior_room_gen(interior2)))
        if storey == '3' or storey == '2 1/2':
            result += ('The third floor, finished with {} flooring, consists of {}'.format(floor_comment_gen(interior3_floor), interior_room_gen(interior3)))
        result += ('Other interior finishes are standard and consistent with the similar type properties in the subject area. The effective age utilized in this appraisal report is based on the MLS listing and pictures provided by the homeowner. '
        'We have assumed the subject property being at least average condition and the norm for the area with other similar properties. ')
    return result

#generate comment for flooring (takes list ['0','1','2'] etc)
#hardwood=0/broadloom=1/ceramic=2/laminate=3
def floor_comment_gen(flooring):
    result = ('')
    floor_type_count = 0
    floor_type_total = len(flooring)
    for i in flooring:
        if i == '0':
            result += ('hardwood')
        elif i == '3':
            result += ('laminate')
        elif i == '1':
            result += ('broadloom')
        elif i == '2':
            result += ('ceramic tiles')
        if floor_type_count < (floor_type_total-2):
            result += (', ')
        elif floor_type_count == (floor_type_total-2):
            result += (', and ')
        floor_type_count += 1
    return result

#for generating exterior finish comment
# brick=0/stone=1/vinyl=2/concrete=3/stucco=4
def exterior_comment_gen(exterior_finish):
    result = ('')
    exterior_type_count = 0
    exterior_type_total = len(exterior_finish)
    for i in exterior_finish:
        if i == '0':
            result += ('brick')
        elif i == '1':
            result += ('stone')
        elif i == '2':
            result += ('vinyl siding')
        elif i == '3':
            result += ('concrete')
        elif i == '4':
            result += ('stucco')
        if exterior_type_count < (exterior_type_total-2):
            result += (', ')
        elif exterior_type_count == (exterior_type_total-2):
            result += (' and ')
        exterior_type_count += 1
    return result

# takes interior1/2/3, a list where odd index is room name and even index is room count, generate 'a foyer, living room, dining room, a master bedroom featuring a full ensuite bathroom, 3 average sized bedrooms and a full bathroom off the main hallway' etc
#['family room', '1', 'den', '0', 'office', '0', 'laundry room', '1', 'master bedroom', '0', 'average sized bedroom', '1', 'full ensuite bathroom', '0', 'full bathroom', '0', '2-piece bathroom', '1'] 
# ['loft', '0', 'den', '1', 'office', '1', 'laundry room', '0', 'master bedroom', '1', 'average sized bedroom', '2', 'full ensuite bathroom', '1', 'full bathroom', '1', '2-piece bathroom', '0']
def interior_room_gen(interior):
    result = ''
    # remove the room from list if 0 > no that type of room
    new_interior = []
    i = 0
    while i < len(interior):
        try:
            int(interior[i])
            if interior[i] != '0':
                new_interior.extend([interior[i-1], interior[i]])
            i += 1
        except:
            i += 1
    interior = new_interior
    types_of_room = int(len(interior)/2)
    i = 0
    suffix = 'a '
    while i < types_of_room:
        # only print comment if there is the room
        if int(interior[i*2+1]) > 0:
            # master bedroom with ensuite comments
            if interior[i*2] == 'master bedroom' and int(interior[i*2+5]) > 0:
                result += (suffix + 'master bedroom featuring a full ensuite bathoom')
                # remove ensuite count by 1, rest for average bedroom
                interior[i*2+5] = str(int(interior[i*2+5])-1)
            #average bedroom with ensuite comments
            if interior[i*2] == 'bedroom' and int(interior[i*2+3]) == 1:
                result += (suffix + interior[i*2+3] + ' averaged sized bedroom featuring a full ensuite bathroom')
            elif interior[i*2] == 'bedroom' and int(interior[i*2+3]) > 1:
                result += (suffix + interior[i*2+3] + ' averaged sized bedrooms featuring full ensuite bathroom')
                interior[i*2+1] = str(int(interior[i*2+1])-int(interior[i*2+3]))
            #reformat bedroom name
            if interior[i*2] == 'bedroom':
                interior[i*2] = 'average sized bedroom'
            # adding all rooms, omitting ensuite bathroom
            if int(interior[i*2+1]) > 0:
                if interior[i*2] == 'full ensuite bathroom' or interior[i*2] == 'master bedroom':
                    pass
                elif interior[i*2] == 'bedroom' or interior[i*2] == 'full bathroom' or interior[i*2] == '2-piece bathroom' or int(interior[i*2+1]) > 1:
                    result += (suffix + interior[i*2+1] + ' ' + interior[i*2])
                else:
                    result += (suffix + interior[i*2])
            else:
                result += suffix
                #formating, and s for plural, and add ','
            suffix = ''
            if int(interior[i*2+1]) > 1 or (interior[i*2] == 'full ensuite bathroom' and int(interior[i*2-1]) > 1):
                suffix += ('s')
            if interior[i*2] == 'full bathroom' and (storey == '1 1/2' or storey == '2' or storey == '2 1/2' or storey == '3') and int(interior[i*2+1]) > 0:
                suffix += (' off the main hallway. ')
            elif i == types_of_room-2:
                suffix += (', and ')
            elif i == types_of_room-1:
                suffix += ('. ')
            else:
                suffix += (', ')
        # special case for ensuite baths
        elif interior[i*2] == 'full ensuite bathroom' and int(interior[i*2+1]) == 0 and i == types_of_room-2:
            suffix = ', and '
        
        i += 1
    result += suffix
    return result
    

def main():
    global storey, ownership, type, sqft
    storey = '2'
    sqft = '999'
    # free = 0 / condo =1
    ownership = '0'
    # property type Det=0/Semi=1/Town=2/Apt=3/Stack=4?
    type = '0'
    #print (interior_info())
    #print (interior1, interior2)
    print (interior_room_gen(['family room', '1','laundry room', '1','average sized bedroom', '1', '2-piece bathroom', '1'] ))
    print (interior_room_gen(['den', '1', 'office', '1', 'master bedroom', '1', 'average sized bedroom', '2', 'full ensuite bathroom', '1', 'full bathroom', '1',]))

if __name__ == "__main__":
    main()




