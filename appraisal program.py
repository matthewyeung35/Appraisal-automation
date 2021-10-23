# For generating sales history
def sales_history():
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
    geo_date =input()
    print ('Geo Name')
    geo_name =input() 
    print ('Geo Price')
    geo_price =input() 
    # collect mls data
    if mls == 'y':
        #create lists to store multiple listing
        mls_no, listing_price, sold_price, mls_date, dom=[], [], [], [], []
        while True:
            print ('MLS number')
            mls_no.append(str(input()))
            print ('MLS list date')
            mls_date.append(str(input()))
            print ('Listing price')
            listing_price.append(str(input()))
            print ('Sold price')
            sold_price.append(str(input()))
            print ('Days on market?')
            dom.append(str(input()))
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
        psa_date =input()
        print ('PSA Buyer')
        psa_buyer =input() 
        print ('PSA Seller')
        psa_seller =input() 
        print ('Geo Price')
        psa_price =input()
    # print out the result
    print ('According to GeoWarehouse, the subject property was registered title on {}, to {}, for a total consideration of ${}.'.format(geo_date, geo_name, geo_price))
    if mls == 'y':
        for no, lprice, sprice, date, d in zip(mls_no, listing_price, sold_price, mls_date, dom):
            print ('As per MLS#{}, the subject property was listed on {} with an asking price of ${} and later was sold for ${} after being on the market for {} days.'.format(no, date, lprice, sprice, d))
    if psa == 'y':
        print ('As per the purchase and sales agreement dated {}, the subject property is under contract between {} (Buyer) and {} (Seller) for a total consideration of ${}.'.format(psa_date, psa_buyer, psa_seller, psa_price))
    
 

            


print("hello world welcome")
sales_history()
