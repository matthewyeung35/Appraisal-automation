 # takes a str money value, return with formatted int
def money_format(money):
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
        date[1] = 'Novmeber'
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

# TODO name formatter, takes in YEUNG, MATTHEW; WHITE, MICHAEL THOMAS; -> return Matthew Yeung & Michael Thomas White
def name_format(name):
    pass


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
    geo_name =input() 
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
            print ('Sold price/Ter/Can/Sus/Cond')
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
        storey = 1
    if ownership == '1':
        print ('Quadrant, Street1, Street2, end/corner/interior')
        condo_location = input().split(',')
    if ownership == '0':
        print ('lot shape, interior/end/corner, backing')
        freehold_location = input().split(',')
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
    print ('Attach=0/Builtin=1/Detach=2/Underg=3/Aboveg=4/None=5')
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
    return

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
        'The subject property is located in close proximity to local area shopping, places of worship, public parks, schools, public transit and {}.'.format(district, city, facilities))
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
        'The subject property is a __ bedroom condominium apartment {} unit{}'
        'As a title search was not conducted, we are not aware of any easements or restrictions that would have a negative impact on value. We were not provided any documentation regarding environmental contamination. '
        'The complex is subject to condo by-laws, lenders should satisfy themselves. Common site area includes fitness centre, swimming pool, guest suites and party room. '.format(street_type, electric, condo_location[3], garage_comment_gen()))
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
        'Environmental hazards were not noted at the property based on appraiser’s visual observation at the time of appraisal viewing. Site is a {} shaped {} lot located on a {}, backing onto a {} '
        'The lot is improved with a {} storey {} dwelling{}The street characteristics include municipal servicing, paved roads with curbs, street lights, and hydro wires placed {}. '
        'Site improvements include covered concrete porch, pathways and a patio at rear. The subject site features fully fenced backyard and average and similar landscaping in comparison to other properties in the area. '
        'The subject property existing use is residential single family and it is the opinion of the appraiser that this activity constitutes the highest and best use. '.format(freehold_location[0], freehold_location[1], street_type, freehold_location[2], storey, freehold_type, garage_comment_gen(), electric,))
    result += adverse_comment

    #TODO basement kitchen comment

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
        if len(adverse) == 0 or (adverse[0] == '1' and (adverse_range[0] == '1000' or adverse_range[0] == '1')):
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
    elif parking_type == '0' or parking_type == '1' or parking_type == '2':
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
    print("hello world welcome")
    takes_info()
    print (sales_history())
    print (neighbour_site())
if __name__ == "__main__":
    main()

