def interior_info():
    result = ('')
    while True:
        try:
            print ('sqft?')
            #sqft = input()
            print ('brick=0/stone=1/vinyl=2/concrete=3/stucco=4')
            exterior_finish = input().split(',')
            #for 1 storey
            interior1 = []
            print('first floor:')
            print ('family room/den/office/laundry')
            storey_rooms = input().split(',')
            interior1.append('family room')
            interior1.append(storey_rooms[0])
            interior1.append('den')
            interior1.append(storey_rooms[1])
            interior1.append('office')
            interior1.append(storey_rooms[2])
            interior1.append('laundry')
            interior1.append(storey_rooms[3])
            interior1.append('bedroom')
            print ('bedroom count?')
            interior1.append(input())
            interior1.append('full bath')
            print ('full bath count?')
            interior1.append(input())
            interior1.append('partial bath')
            print ('partial bath count?')
            interior1.append(input())
            print ('hardwood=0/broadloom=1/ceramic=2/laminate=3')
            interior1_floor = input().split(',')
            # for 2 storey
            if storey != '1':
                interior2 = []
                print('second floor:')
                print ('loft/den/office/laundry')
                storey_rooms = input().split(',')
                interior2.append('loft')
                interior2.append(storey_rooms[0])
                interior2.append('den')
                interior2.append(storey_rooms[1])
                interior2.append('office')
                interior2.append(storey_rooms[2])
                interior1.append('laundry')
                interior1.append(storey_rooms[3])
                interior2.append('bedroom')
                print ('bedroom count?')
                interior2.append(input())
                interior2.append('full bath')
                print ('full bath count?')
                interior2.append(input())
                interior2.append('partial bath')
                print ('partial bath count?')
                interior2.append(input())
                print ('hardwood=0/broadloom=1/ceramic=2/laminate=3')
                interior2_floor = input().split(',')
            if storey == '2 1/2 ' or storey == '3':
                interior3=[]
                print('third floor:')
                print ('loft/den/office/laundry')
                storey_rooms = input().split(',')
                interior2.append('loft')
                interior2.append(storey_rooms[0])
                interior2.append('den')
                interior2.append(storey_rooms[1])
                interior2.append('office')
                interior2.append(storey_rooms[2])
                interior1.append('laundry')
                interior1.append(storey_rooms[3])
                interior2.append('bedroom')
                print ('bedroom count?')
                interior2.append(input())
                interior2.append('full bath')
                print ('full bath count?')
                interior2.append(input())
                interior2.append('partial bath')
                print ('partial bath count?')
                print ('hardwood=0/broadloom=1/ceramic=3/laminate=4')
                interior3_floor = input().split(',')
        except IndexError:
            print ('Invalid input')
        else:
            break

    # interior finishes
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
        'The main floor, finished with {} flooring consists of a foyer, living room, dining room, kitchen, and a 2-piece bathroom. '.format(storey, house_name, sqft, exterior_comment_gen(exterior_finish), floor_comment_gen(interior1_floor)))
        if storey != '1':
            result += ('The second floor, finished with {} flooring, consists of a master bedroom featuring a full ensuite bathroom, 2 average sized bedrooms and a full bathroom off the main hallway. '.format(floor_comment_gen(interior2_floor)))
        if storey == '3' or storey == '2 1/2':
            result += ('The third floor, finished with {} flooring, consists of a master bedroom featuring a full ensuite bathroom, 2 average sized bedrooms and a full bathroom off the main hallway. '.format(floor_comment_gen(interior3_floor)))
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



def main():
    global storey, ownership, type, sqft
    storey = '2'
    sqft = '999'
    # free = 0 / condo =1
    ownership = '0'
    # property type Det=0/Semi=1/Town=2/Apt=3/Stack=4?
    type = '0'
    print (interior_info())
    #print(floor_comment_gen(['0','1','2']))
    #print(exterior_comment_gen(['4']))

if __name__ == "__main__":
    main()




