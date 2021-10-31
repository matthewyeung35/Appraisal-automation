 # takes a str money value, return with formatted int
def money_format(money):
    if ',' in money:
        return money
    else:
        money = int(money)
        return '{:,}'.format(money)

# date formater, input 2021-01-01, return January 1, 2021
def date_format(date):
    date = date.split('-')
    if date[1] == '01':
        date[1] = 'January'
    elif date[1] =='02':
        date[1] = 'Febraury'
    elif date[1] =='03':
        date[1] = 'March'
    elif date[1] =='04':
        date[1] = 'April'
    elif date[1] =='05':
        date[1] = 'May'
    elif date[1] =='06':
        date[1] = 'June'
    elif date[1] =='07':
        date[1] = 'July'
    elif date[1] =='08':
        date[1] = 'August'
    elif date[1] =='09':
        date[1] = 'September'
    elif date[1] =='10':
        date[1] = 'October'
    elif date[1] =='11':
        date[1] = 'Novmember'
    elif date[1] =='12':
        date[1] = 'Decmeber'
    if date[2] == '01':
        date[2] = '1'
    elif date[2] == '02':
        date[2] = '2'
    elif date[2] == '02':
        date[2] = '2'
    elif date[2] == '03':
        date[2] = '3'
    elif date[2] == '04':
        date[2] = '4'
    elif date[2] == '05':
        date[2] = '5'
    elif date[2] == '06':
        date[2] = '6'
    elif date[2] == '07':
        date[2] = '7'
    elif date[2] == '08':
        date[2] = '8'
    elif date[2] == '09':
        date[2] = '2'
    return ('{} {}, {}'.format(date[1],date[2], date[0]))

#name formatter, takes in YEUNG, MATTHEW; WHITE, MICHAEL THOMAS; -> return Matthew Yeung & Michael Thomas White
def name_format(name):
    result = ('')
    temp_list=[]
    #if more than 1 name, use a list to separate names, else create a list with 1 element
    if ';' in name:
        name = name.split(';')
    else:
        temp_list.append(name)
        name = temp_list 
    # remove the empty element created by last ;
    if len(name) > 1:
        name.pop()
    i_count = 0
    for i in name:
        if i_count >= 1:
            i = i.strip()
        # if in , format, swap last anf first name
        if ',' in i:
            exchange_name = i.split(',')
            exchange_name = exchange_name[1].strip() + ' ' + exchange_name[0].strip()
        else:
            exchange_name = i
        name[i_count] = exchange_name
        i_count += 1
    for i in name:
        result += i
        result += (' & ')
    result = result[:-3]
    return result.title()

# For generating sales history
def sales_history():
    result = ('')
    #check listing
    while True:
        print('Is there a MLS? y/n')
        mls = input()
        if (mls == 'y') or (mls == 'n'):
            break
        else:
            print ('Invalid input')
    #check psa
    while True:
        print('Is there a PSA? y/n')
        psa = input()
        if (mls == 'y') or (mls == 'n'):
            break
        
        else:
            print ('Invalid input')
    # collect geowarehouse data
    print ('Geo Date')
    geo_date =date_format(input())
    print ('Geo Name')
    geo_name = name_format(input())
    print ('Geo Price')
    geo_price = input()
    result += ('According to GeoWarehouse, the subject property was registered title on {}, to {}, for a total consideration of ${}.\n'.format(geo_date, geo_name, money_format(geo_price)))
    # collect mls data
    if mls == 'y':
        #create lists to store multiple listing
        while True:
            print ('MLS number')
            mls_no = input()
            print ('MLS list date')
            mls_date = date_format(input())
            print ('Listing price')
            listing_price = money_format(input())
            print ('Sold price/Ter/Can/Sus/Cond/Exp/Act')
            sold_price = input()
            if sold_price != 'cond':
                print ('Days on market?')
                dom = input()
            # check if mls is terminated/cancelled etc
            if sold_price == 'cond':
                result += ('As per MLS#{}, the subject property was listed on {} with an asking price of ${} and later was sold conditionally. \n'.format(mls_no, mls_date, listing_price))
            elif sold_price == 'ter':
                 result += ('As per MLS#{}, the subject property was listed on {} with an asking price of ${} and later was terminated after being on the market for {} days. \n'.format(mls_no, mls_date, listing_price, dom))
            elif sold_price == 'can':
                    result += ('As per MLS#{}, the subject property was listed on {} with an asking price of ${} and later was cancelled after being on the market for {} days. \n'.format(mls_no, mls_date, listing_price, dom))
            elif sold_price == 'sus':
                result += ('As per MLS#{}, the subject property was listed on {} with an asking price of ${} and later was suspeneded after being on the market for {} days. \n'.format(mls_no, mls_date, listing_price, dom))
            elif sold_price == 'exp':
                result += ('As per MLS#{}, the subject property was listed on {} with an asking price of ${} and later was expired after being on the market for {} days. \n'.format(mls_no, mls_date, listing_price, dom))           
            elif sold_price == 'act':
                result += ('As per MLS#{}, the subject property was listed on {} with an asking price of ${} and is currently listed for sale. \n'.format(mls_no, mls_date, listing_price))  
            else:
                result += ('As per MLS#{}, the subject property was listed on {} with an asking price of ${} and later was sold for ${} after being on the market for {} days. \n'.format(mls_no, mls_date, listing_price, money_format(sold_price), dom))
            #more mls entry if neccessary
            while True:
                print('Is there more MLS? y/n')
                more_mls = input()
                if (mls == 'y') or (mls == 'n'):
                    break
                else:
                    print ('Invalid input')
            if more_mls == 'y':
                print ('Input data for more mls')
            else:
                break
    elif mls == 'n':
        result += ('Currently, there is no MLS listing for this property. \n')
    #collect psa data
    if psa == 'y':   
        print ('PSA Date')
        psa_date = date_format(input())
        print ('PSA Buyer')
        psa_buyer =input() 
        print ('PSA Seller')
        psa_seller =input() 
        print ('PSA Price')
        psa_price = money_format(input())
        result += ('As per the purchase and sales agreement dated {}, the subject property is under contract between {} (Buyer) and {} (Seller) for a total consideration of ${}.'.format(psa_date, psa_buyer, psa_seller, psa_price)) 
    result += ('\n\n')
    return result
 
# get property information
def takes_info():
    global city, district, ownership, type, condo_location, occupy, adverse, facilities, townhouse_location, adverse_range, nuclear_station, street_type, storey, electric, parking_type, parking_no, lease, basement, freehold_location
    print ('City?')
    city = input()
    print ('District')
    district = input()
    # type of property
    print ('Free=0/condo=1?')
    ownership = input()
    while True:
        print ('property type Det=0/Semi=1/Town=2/Apt=3/Stack=4?')
        type = input()
        if type == '0' and ownership == '1' or type == '1' and ownership =='1' or type =='3' and ownership =='0' or type == '4' and ownership == '0':
            print ('Invalid input')
        else:
            break
    #no. of storey
    if type != '3':
        print ('How many storey?')
        storey = input()
    else:
        storey = '1'
    if ownership == '1':
        while True:
            print ('Quadrant, Street1, Street2, end/corner/interior')
            condo_location = input().split(',')
            if len(condo_location) == 4:
                break
            else:
                print ('invalid input')
    if ownership == '0':
        while True:
            print ('lot shape, interior/end/corner, backing')
            freehold_location = input().split(',')
            if len(freehold_location) == 3:
                break
            else:
                print ('invalid input')
    if ownership =='0' and type == '2':
        print ('townhouse location?')
        townhouse_location = input()
    #street type
    print ('Commercial=0/Residential=1/Main=2/Commuter=3 front street')
    street_type = input()
    if street_type == '0':
        street_type = 'commercial street'
    elif street_type == '1':
        street_type = 'residential street'
    elif street_type == '2':
        street_type = 'main road'
    elif street_type == '3':
        street_type = 'commuter street'
    # occupied?
    print ('Owner=0/Tenant=1/Both=2/vacant=3')
    occupy = input()
    # parking
    print ('Attach=0/Builtin=1/Detach=2/Underg=3/Aboveg=4/None+Driveway=5/NoneNone=6')
    parking_type = input ()
    print ('How many parking space?')
    parking_no = input()
    # basement
    if type != '3':
        print('finished=0/partly=1/unfin=2/none=3')
        basement = input()
    # adverse or no
    print ('airport=0/railway=1/main=2/commuter=3/hydrolane=4/nuclear=5' )
    adverse = input().split(',')
    # ask for range if have airport/railway/lane/nuclear
    adverse_range = []
    if len(adverse[0]) != 0:
        for i in adverse:
            if i =='0':
                print ('Airport range(KM)?')
                adverse_range.append(input())
            elif i =='1':
                print ('Railway range(M)?')
                adverse_range.append(input())
            elif i == '2' or i == '3':
                adverse_range.append('')
            elif i =='4':
                print ('Hydro lane range(M)?')
                adverse_range.append(input())
            elif i =='5':
                print ('Nuclear range(KM)?')
                adverse_range.append(input())
                print ('Pickering=0/Darlington=1')
                nuclear_station = input()
    print ('Nearby park/school')
    facilities = input()
    print ('electric underground=0/overhead=1')
    electric = input()
    if electric == '0':
        electric = 'underground'
    else:
        electric = 'overhead'
    #lease required?
    print ('leased required? y/n')
    lease = input()

# generate basement comments
def basement_comment_gen():
    print ('Basement')
    global basement_kitchen
    basement_kitchen = 0 
    if basement == '3':
        return ('None; Interior not viewed by the appraiser at the request of the lender due to safety and health concerns impacted by the Co-Vid 19 Virus. It is unknown if there was water seepage at the time of appraisal. Appraisal is based on a sound foundation.')
    elif basement == '2':
        return ('The basement is unfinished featuring a mech area.  Interior not viewed by the appraiser at the request of the lender due to safety and health concerns impacted by the Co-Vid 19 Virus. '
        'It is unknown if there was water seepage at the time of appraisal. Appraisal is based on a sound foundation. ')
    else:
        basement_interior = []
        print('separate entrance?')
        basement_rooms = input()
        basement_interior.extend(['separate entrance', basement_rooms])
        print('living/dining/kitchen')
        basement_rooms = input().split(',')
        if basement_rooms[2] == '1':
            basement_kitchen = 1
        basement_interior.extend(['living room', basement_rooms[0] , 'dining room', basement_rooms[1], 'kitchen', basement_rooms[2]])
        print('rec/family/den/laundry')
        basement_rooms = input().split(',')
        basement_interior.extend(['recreational room', basement_rooms[0] , 'family room', basement_rooms[1], 'den', basement_rooms[2], 'laundry room', basement_rooms[3]])
        print('bed/full bath/2-piece bath')
        basement_rooms = input().split(',')
        basement_interior.extend(['bedroom', basement_rooms[0] , 'full bathroom', basement_rooms[1], '2-piece bathroom', basement_rooms[2]])
        # remove the room from list if 0 > no that type of room
        new_interior = []
        i = 0
        while i < len(basement_interior):
            try:
                int(basement_interior[i])
                if basement_interior[i] != '0':
                    new_interior.extend([basement_interior[i-1], basement_interior[i]])
                i += 1
            except:
                i += 1
        basement_interior = new_interior
        types_of_room = int(len(basement_interior)/2)
        i = 0
        result = ''
        suffix = 'a '
        while i < types_of_room:
            result += suffix
            if int(basement_interior[i*2+1]) > 1 or basement_interior[i*2] == 'bedroom' or basement_interior[i*2] == 'full bathroom' or basement_interior[i*2] == '2-piece bathroom':
                result += basement_interior[i*2+1] + ' ' + basement_interior[i*2]
            else:
                result += basement_interior[i*2]
            suffix = ''
            if int(basement_interior[i*2+1]) > 1:
                suffix += ('s')
            suffix += (', ')
            i += 1
        result += suffix
        if basement == '0':
            result = ('The basement is fully finished featuring {}and mech area. Interior not viewed by the appraiser at the request of the lender due to safety and health concerns impacted by the Co-Vid 19 Virus. '
            'It is unknown if there was water seepage at the time of appraisal. Appraisal is based on a sound foundation. '.format(result))
        elif basement == '1':
            result = ('The basement is partly finished featuring {}and mech area. Interior not viewed by the appraiser at the request of the lender due to safety and health concerns impacted by the Co-Vid 19 Virus. '
            'It is unknown if there was water seepage at the time of appraisal. Appraisal is based on a sound foundation. '.format(result))
        result += ('\n\n')
        return result

# generate interior comments
def interior_info():
    global interior1, interior2, interior3, total_bed
    result = ('')
    while True:
        try:
            print ('sqft?')
            sqft = input()
            print ('brick=0/stone=1/vinyl=2/concrete=3/stucco=4')
            exterior_finish = input().split(',')
            #for 1 storey
            interior1 = ['foyer', '1']
            print('first floor:')
            print ('living+dining+kitchen? (0 or 1)')
            storey_rooms = input()
            if storey_rooms == '1':
                interior1.extend(['living room', '1', 'dining room', '1', 'kitchen', '1'])
            print ('family room/den/office/laundry')
            storey_rooms = input().split(',')
            interior1.extend(['family room', storey_rooms[0] , 'den' , storey_rooms[1] , 'office' , storey_rooms[2] , 'laundry room' , storey_rooms[3]])
            print ('master bed/ average bed')
            storey_rooms = input().split(',')
            total_bed = int(storey_rooms[0]) + int(storey_rooms[1])
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
                if storey_rooms == '1':
                    interior2.extend(['living', '1', 'dining', '1', 'kitchen', '1'])
                if input == '1':
                    interior2.extend(['living', '1', 'dining', '1', 'kitchen', '1'])
                print ('loft/den/office/laundry')
                storey_rooms = input().split(',')
                if ownership == '1' and type == '3':
                    interior2.extend(['loft', storey_rooms[0] , 'den' , storey_rooms[1] , 'office' , storey_rooms[2] , 'ensuite washer/dryer' , storey_rooms[3]])
                else:
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
                print ('hardwood=0/broadloom=1/ceramic=2/laminate=3')
                interior3_floor = input().split(',')
        except IndexError:
            print ('Invalid input')
        else:
            break

    #interior finishes
    print ('potlight/crown moulding?')
    interior_finishes = input()
  
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
        # interior finishes comment
        result += interior_finishes_gen(interior_finishes)
        result += ('Other interior finishes are standard and consistent with the similar type properties in the subject area. The effective age utilized in this appraisal report is based on the MLS listing and pictures provided by the homeowner. '
        'We have assumed the subject property being at least average condition and the norm for the area with other similar properties. ')
    elif ownership == '1' and type == '2':
        result += ('The subject is a {} storey condominium townhouse {} unit containing approximately {} square feet of living space and is assumed to be in average physical condition at time of appraisal. '
        'The exterior of the home is finished with mostly {}. The main floor, finished with {}, consists of {}'. format(storey, condo_location[3], sqft, exterior_comment_gen(exterior_finish), floor_comment_gen(interior1_floor), interior_room_gen(interior1)))
        if storey != '1':
            result += ('The second floor, finished with {} flooring, consists of {}'.format(floor_comment_gen(interior2_floor), interior_room_gen(interior2)))
        if storey == '3' or storey == '2 1/2':
            result += ('The third floor, finished with {} flooring, consists of {}'.format(floor_comment_gen(interior3_floor), interior_room_gen(interior3)))
        result += interior_finishes_gen(interior_finishes)
        result += ('Other interior finishes are standard and consistent with similar type units in the condominium complex. The effective age utilized in this appraisal report is based on the MLS listing and pictures provided by the homeowner. '
        'We have assumed the subject property being at least average condition and the norm for the area with other similar properties. ')
    elif ownership == '1' and type == '4':
        result += ('The subject is a {} storey condominium stacked townhouse {} unit containing approximately {} square feet of living space and is assumed to be in average physical condition at time of appraisal. '
        'The exterior of the home is finished with mostly {}. The main floor, finished with {}, consists of {}'. format(storey, condo_location[3], sqft, exterior_comment_gen(exterior_finish), floor_comment_gen(interior1_floor), interior_room_gen(interior1)))
        if storey != '1':
            result += ('The second floor, finished with {} flooring, consists of {}'.format(floor_comment_gen(interior2_floor), interior_room_gen(interior2)))
        if storey == '3' or storey == '2 1/2':
            result += ('The third floor, finished with {} flooring, consists of {}'.format(floor_comment_gen(interior3_floor), interior_room_gen(interior3)))
        result += interior_finishes_gen(interior_finishes)
        result += ('Other interior finishes are standard and consistent with similar type units in the condominium complex. The effective age utilized in this appraisal report is based on the MLS listing and pictures provided by the homeowner. '
        'We have assumed the subject property being at least average condition and the norm for the area with other similar properties. ')
    elif ownership == '1' and type == '3':
        result += ('The subject is a {} bedroom condominium apartment {} unit containing approximately {} square feet of living space and is assumed to be in average physical condition at time of appraisal. '
        'The floor plan consists of {}. Interior is finished with laminate flooring in the living room, dining room and bedrooms, ceramic tiles in the kitchen, bathroom and foyer. '
        'Interior finishes are standard and consistent with similar type units in the condominium complex. '. format(total_bed, condo_location[3], sqft, interior_room_gen(interior1)))
        result += interior_finishes_gen(interior_finishes)
        result += ('The effective age utilized in this appraisal report is based on the MLS listing and pictures provided by the homeowner. We have assumed the subject property being at least average condition and the norm for the area with other similar properties. ')
    result += ('\n\n')
    return result

#generate interior finishes comment
def interior_finishes_gen(interior_finishes):
    if interior_finishes == '0,1':
        return ('Interior upgrades include crown mouldings. ')
    elif interior_finishes == '1,0':
        return ('Interior upgrades include potlights. ')
    elif interior_finishes == '1,1': 
        return ('Interior upgrades include potlights and crown mouldings. ')
    else:
        return ('')


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
#['family room', '1', 'den', '0', 'office', '0', 'laundry room', '1', 'master bedroom', '0', 'bedroom', '1', 'full ensuite bathroom', '0', 'full bathroom', '0', '2-piece bathroom', '1'] 
# ['loft', '0', 'den', '1', 'office', '1', 'laundry room', '0', 'master bedroom', '1', 'bedroom', '2', 'full ensuite bathroom', '1', 'full bathroom', '1', '2-piece bathroom', '0']
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
        if interior[i*2] != 'full ensuite bathroom':
            # master bedroom with ensuite comments
            if interior[i*2] == 'master bedroom' and interior[i*2+4] == 'full ensuite bathroom' and int(interior[i*2+5]) > 0:
                result += (suffix + 'master bedroom featuring a full ensuite bathoom')
                interior[i*2+1] = str(int(interior[i*2+1])-1)
                # remove ensuite count by 1, rest for average bedroom
                interior[i*2+5] = str(int(interior[i*2+5])-1)
            #average bedroom with ensuite comments
            elif interior[i*2] == 'bedroom' and interior[i*2+2] == 'full ensuite bathroom' and int(interior[i*2+3]) == 1:
                result += (suffix + interior[i*2+3] + ' averaged sized bedroom featuring a full ensuite bathroom')
                interior[i*2+1] = str(int(interior[i*2+1])-1)
            elif interior[i*2] == 'bedroom' and interior[i*2+2] == 'full ensuite bathroom' and int(interior[i*2+3]) > 1:
                result += (suffix + interior[i*2+3] + ' averaged sized bedrooms featuring full ensuite bathroom')
                interior[i*2+1] = str(int(interior[i*2+1])-int(interior[i*2+3]))
            #reformat bedroom name
            if interior[i*2] == 'bedroom':
                interior[i*2] = 'average sized bedroom'
            # adding all rooms, omitting ensuite bathroom
            if  int(interior[i*2+1]) > 0 :
                if interior[i*2] == '2-piece bathroom' and int(interior[i*2+1]) == 1:
                    result += (suffix + 'a ' + interior[i*2])
                elif interior[i*2] == 'average sized bedroom' or interior[i*2] == 'full bathroom' or int(interior[i*2+1]) > 1:
                    result += (suffix + interior[i*2+1] + ' ' + interior[i*2])
                else:
                    result += (suffix + interior[i*2])
                #formating, and s for plural, and add ','
            suffix = ''
            if int(interior[i*2+1]) > 1:
                suffix += ('s')
            if interior[i*2] == 'full bathroom' and (storey == '1 1/2' or storey == '2' or storey == '2 1/2' or storey == '3'):
                suffix += (' off the main hallway. ')
            elif i == types_of_room-2:
                suffix += (', and ')
            elif i == types_of_room-1:
                suffix += ('. ')
            else:
                suffix += (', ')
        # special case for ensuite baths
        elif interior[i*2] == 'full ensuite bathroom':
            suffix = ''
            if int(interior[i*2-1]) > 1:
                suffix += ('s')
            if i == types_of_room-2:
                suffix += ', and '
            elif i == types_of_room-1:
                suffix += ('. ')
            else:
                suffix += (', ')
        
        i += 1
    result += suffix
    return result

# for neighbourhood and site comments
def neighbour_site():
    result = ('')
    # check demand
    if type == '3':
        demand = 'stable'
    else:
        demand ='increasing'
    #condo neighourhood
    if ownership == '1':
        result += ("Neighbourhood\nThe subject area is located within the {} quadrant of {} and {}, in the MLS district known as '{}' in the City of {}. The neighbourhood is comprised of a mix of residential, "
        'commercial, as well as condominium properties. The immediate area consists mainly of residential established properties ranging up to _ years old in varying age, size, and condition. Newly built condominium buildings are also noted in the area. '
        'Based on the average days on market on the recent MLS listings, the demands for properties in this neighborhood is considered average to good. Based on research on recent MLS listings, '
        'the market trend in the immediate area was {} at the time of appraisal. '
        "The subject is in close proximity to local area shopping centres, {}, public transit, public schools, and parks. ".format(condo_location[0], condo_location[1], condo_location[2], district, city, demand, facilities))
    else:
        #freehold neighbourhood
        result += ("Neighbourhood\nThe subject area is located within the MLS district known as '{}' in the City of {}. The neighbourhood is comprised of a mix of residential, commercial, as well as condominium properties. "
        'The immediate area consists mainly of residential established properties ranging up to _ years old in varying age, size and condition. Newer built condominium developments were also noted in the general area. '
        'Based on average days on market on the recent MLS listings, the demand for properties in this neighborhood is considered average to good. Based on research on recent MLS listings, the market trend in the immediate area is considered increasing at the time of appraisal. '
        'The subject property is located in close proximity to local area shopping, places of worship, public parks, schools, public transit and {}. '.format(district, city, facilities))
    adverse_comment = adverse_comment_gen()
    result += adverse_comment + ('\n\nSite\n')
    #condo townhouse site
    if ownership == '1' and type == '2':
        result += ('Appraiser did not note any wind turbines at the property at the time of appraisal. Underground storage utility were not visible to the appraiser on the subject site at time of appraisal viewing. '
        'Environmental hazards were not noted at the property based on appraiser’s visual observation at the time of appraisal viewing. '
        'The subject site is improved with a condominium townhouse complex located on a {}. The street characteristics include municipal servicing, paved roads with curbs, street lights, and hydro wires placed {}. '
        'The subject property is a {} storey condominium townhouse {} unit{}'
        'As a title search was not conducted, we are not aware of any easements or restrictions that would have a negative impact on value. '
        'We were not provided any documentation regarding environmental contamination. The complex is subject to condo by-laws, lenders should satisfy themselves. '.format(street_type, electric, storey, condo_location[3], garage_comment_gen()))
    #condo apt
    elif ownership == '1' and type =='3':
        result += ('Appraiser did not note any wind turbines at the property at the time of appraisal. Underground storage utility were not visible to the appraiser on the subject site at time of appraisal viewing. '
        'Environmental hazards were not noted at the property based on appraiser’s visual observation at the time of appraisal viewing. The subject site is improved with a high rise condominium complex located on a {}. '
        'The street characteristics include municipal servicing, paved roads with curbs, street lights, and hydro wires placed {}. '
        'The subject property is a {} bedroom condominium apartment {} unit{}'
        'As a title search was not conducted, we are not aware of any easements or restrictions that would have a negative impact on value. We were not provided any documentation regarding environmental contamination. '
        'The complex is subject to condo by-laws, lenders should satisfy themselves. Common site area includes fitness centre, swimming pool, guest suites and party room. '.format(street_type, electric, total_bed, condo_location[3], garage_comment_gen()))
    #stack townhouse
    elif ownership == '1' and type == '4':
        result += ('Appraiser did not note any wind turbines at the property at the time of appraisal. Underground storage utility were not visible to the appraiser on the subject site at time of appraisal viewing. '
        'Environmental hazards were not noted at the property based on appraiser’s visual observation at the time of appraisal viewing. '
        'The subject site is improved with a condominium townhouse complex located on a {}. The street characteristics include municipal servicing, paved roads with curbs, street lights, and hydro wires placed {}. '
        'The subject property is a {} storey condominium stacked townhouse {} unit{}'
        'As a title search was not conducted, we are not aware of any easements or restrictions that would have a negative impact on value. '
        'We were not provided any documentation regarding environmental contamination. The complex is subject to condo by-laws, lenders should satisfy themselves. '.format(street_type, electric, storey, condo_location[3], garage_comment_gen()))
    #freehold
    elif ownership == '0':
        # naming the type of house
        if type == '0':
            freehold_type = 'detached'
        elif type == '1':
            freehold_type = 'semi-detached'
        elif type == '2':
            freehold_type = 'townhouse'
        result += ('Appraiser did not note any wind turbines at the property at the time of appraisal. Underground oil storage utility were not visible to the appraiser at time of appraisal. '
        'Environmental hazards were not noted at the property based on appraiser’s visual observation at the time of appraisal viewing. Site is a {} shaped {} lot located on a {}, backing onto {}. '
        'The lot is improved with a {} storey {} dwelling{}The street characteristics include municipal servicing, paved roads with curbs, street lights, and hydro wires placed {}. '
        'Site improvements include covered concrete porch, pathways and a patio at rear. The subject site features fully fenced backyard and average and similar landscaping in comparison to other properties in the area. '
        'The subject property existing use is residential single family and it is the opinion of the appraiser that this activity constitutes the highest and best use. '.format(freehold_location[0], freehold_location[1], street_type, freehold_location[2], storey, freehold_type, garage_comment_gen(), electric,))
    result += adverse_comment

    #TODO basement kitchen comment
    if basement_kitchen == 1:
        pass


    #tenant comment
    if occupy == '1':
        if ownership == '0':
            ownership_name = 'Fee Simple'
        else:
            ownership_name = 'Condominium Ownership'
        result += ('As per the homeowner, the subject property was tenant occupied at time of appraisal. At the request of the client, the property is being valued in ' + ownership_name) 
        if lease == 'n':
            result += (', and the Leased Fee value has not been addressed in this assignment.')
        else:
            result += ('.')
    return result

# generate adverse comment
def adverse_comment_gen():
    result = ('')
    # for apartment adverse
    no_adverse = 1
    if type == '3':
        for i in adverse:
            if i == '1':
                result += ('Railroad tracks were also noted within the general area of the subject property. ')
        adverse_no = 0
        for i in adverse:
            if i == '0':
                if city == 'Ottawa':
                    result += ('Adversely, the subject property is situated within ' + adverse_distance_convert(adverse_range[adverse_no]) + ' of Ottawa International Airport and is subject to higher air traffic noises during operational hours. ')
                else:
                    result +=('Adversely, the subject property is situated within ' + adverse_distance_convert(adverse_range[adverse_no]) + ' of Toronto Pearson Airport and is subject to higher air traffic noises during operational hours. ')
                no_adverse = 0
            if i == '4':
                if no_adverse == 1:
                    result += ('Adversely, the subject property issituated within ' + adverse_distance_convert(adverse_range[adverse_no]) + ' of hydro lanes. ')
                    no_adverse = 0
                else:
                    result += ('The subject property is also situated within ' + adverse_distance_convert(adverse_range[adverse_no]) + ' of hydro lanes. ')
            if i == '5':
                if no_adverse == 1:
                    if nuclear_station == '0':
                        result += ('Adversely, the subject property is situated within ' + adverse_distance_convert(adverse_range[adverse_no]) + ' of Pickering Nuclear Generating Station. ')
                    else :
                        result += ('Adversely, the subject property is situated within ' + adverse_distance_convert(adverse_range[adverse_no]) + ' of Darlington Nuclear Generating Station. ')
                    no_adverse = 0
                else:
                    if nuclear_station == '0':
                        result += ('The subject property is also situated within ' + adverse_distance_convert(adverse_range[adverse_no]) + ' of Pickering Nuclear Generating Station. ')
                    else :
                        result += ('The subject property is also situated within ' + adverse_distance_convert(adverse_range[adverse_no]) + ' of Darlington Nuclear Generating Station. ')                   
            adverse_no += 1
        if no_adverse == 1:
            result += ('The Appraiser did not notice any functional or external obsolescence at the time of the site visit. ')
        else:
            result += ('See plot map. ')
    else :
    # non apt adverse
        adverse_no = 0
        # for out of range railway, no adverse
        if len(adverse) == 1 and adverse[0] == '1' and (adverse_range[0] == '1000' or adverse_range[0] == '1'):
            result += ('Railroad tracks were also noted within the general area of the subject property. ')
        if (len(adverse) == 1 and (adverse[0] not in ['0','1','2','3','4','5'])) or (adverse[0] == '1' and (adverse_range[0] == '1000' or adverse_range[0] == '1')):
            result += ('The Appraiser did not notice any functional or external obsolescence at the time of the site visit. ')
        else:
            no_of_adverse = len(adverse)
            adverse_no = 0
            #with adverse and out of range railways
            for i in adverse:
                if i == '1' and (adverse_range[adverse_no] == '1000' or adverse_range[adverse_no] == '1'):
                    result += ('Railroad tracks were also noted within the general area of the subject property. ')
                    break
                adverse_no += 1
            adverse_no = 0
            result += ('Adversely, the subject property is ')
            for i in adverse:
                print (no_of_adverse)
                # if more than 1 adverse
                if no_of_adverse < len(adverse) and not (i == '1' and (adverse_range[adverse_no] == '1000' or adverse_range[adverse_no] == '1')):
                    result += ('The subject property is also ')
                no_of_adverse -=1
                # add adverse comments
                if i == '0':
                    if city == 'Ottawa':
                        result += ('situated within ' + adverse_distance_convert(adverse_range[adverse_no]) + ' of Ottawa International Airport and is subject to higher air traffic noises during operational hours. ')
                    else:
                        result +=('situated within ' + adverse_distance_convert(adverse_range[adverse_no]) + ' of Toronto Pearson Airport and is subject to higher air traffic noises during operational hours. ')
                elif i == '1':
                    if adverse_range[adverse_no] != '1000' and adverse_range[adverse_no] != '1':
                        result += ('situated within ' + adverse_distance_convert(adverse_range[adverse_no]) + ' of railroad tracks and is subject to railroad noises during operational hours. ')
                    else:
                        no_of_adverse +=1
                elif i == '2':
                    result += ('located on a main road, which is subjected to busy and noisy traffic during peak hours. ')
                elif i == '3':
                    result += ('located on a commuter street, which is subjected to busy and noisy traffic during peak hours. ')
                elif i == '4':
                    result += ('situated within ' + adverse_distance_convert(adverse_range[adverse_no]) + ' of hydro lanes. ')
                elif i == '5':
                    if nuclear_station == '0':
                        result += ('situated within ' + adverse_distance_convert(adverse_range[adverse_no]) + ' of Pickering Nuclear Generating Station. ')
                    else :
                        result += ('situated within ' + adverse_distance_convert(adverse_range[adverse_no]) + ' of Darlington Nuclear Generating Station. ')
                adverse_no +=1
            result += ('See plot map. ')
    return result

#convert garage id to text 
# Attach=0/Builtin=1/Detach=2/Underg=3/Aboveg=4/None=5
def garage_comment_gen():
    result = ('')
    if parking_type == '3' or parking_type =='4':
        result += (' that includes ')
    elif parking_type == '0' or parking_type == '1' or parking_type == '2' or parking_type =='5':
        result += (' featuring a ')
    result += parking_no
    if parking_type == '0':
        result += (' car attached ')
    elif parking_type == '1':
        result += (' car built-in ')
    elif parking_type == '2':
        result += (' car detached ')
    elif parking_type == '3':
        result += (' underground parking space and a locker***. ')
    elif parking_type == '4':
        result += (' surface parking space. ')
    elif parking_type == '5':
        result += ('a private asphalt-surfaced driveway. ')
    else :
        result += ('. ')
    if parking_type == '0' or parking_type == '1' or parking_type == '2':
        result += ('garage on a private asphalt-surfaced driveway. ')
    return result

    
    

# for adverse_comment, add M/KM/close proxmity comment
def adverse_distance_convert(dist):
    if dist == '200':
        return ('close proximity')
    elif dist == '5':
        return ('5KM')
    elif dist == '10':
        return ('10KM')
    elif dist == '500':
        return ('500M')
    elif dist == '1000':
        return ('1KM')
    elif dist == '1':
        return ('1KM')


def main():
    result = ''
    print("Welcome")
    takes_info()
    result += (basement_comment_gen())
    result += (interior_info())
    result += (sales_history())
    result += (neighbour_site())
    text_file = open("Output.txt", "w")
    text_file.write(result)
    text_file.close()

    #------testing stuff----------
    '''
    global storey
    storey = 2
    interior = ['loft', '1', 'den', '1', 'office', '1', 'laundry room', '0', 'master bedroom', '1', 'bedroom', '3', 'full ensuite bathroom', '1', 'full bathroom', '1', '2-piece bathroom', '0']
    print(interior_room_gen(interior))
    '''

if __name__ == "__main__":
    main()

