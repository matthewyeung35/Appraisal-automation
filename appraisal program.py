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
    print ('City?')
    city = input()
    print ('District')
    district = input()
    print ('Free=0/condo=1?')
    ownership = input()
    while True:
        print ('property type Det=0/Semi=1/Town=2/Apt=3/Stack=4?')
        type = input()
        if type == ('0') and ownership == '1' or type == ('1') and ownership =='1' or type =='3' and ownership =='0' or type == '4' and ownership == '0':
            print ('Invalid input')
        else:
            break
    print ('Owner/Tenant/Both?')
    living = input()
    print ('adverse? y/n')
    adverse = input()
    if adverse == 'y':
        print ('airport=0/railway=1/main=2/commuter=3/hydrolane=4/nuclear=5' )
        what_adverse = input().split(' ')



        
    




def main():
    print("hello world welcome")
    #print (sales_history())
    takes_info()
if __name__ == "__main__":
    main()

