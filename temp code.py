def main():
    interior_finishes = ''
    print ('potlight/crown moulding?')
    interior_finishes = input()
    if interior_finishes == '0,1':
        result += ('Interior upgrades include crown mouldings. ')
    elif interior_finishes == '1,0':
        result += ('Interior upgrades include potlights. ')
    elif interior_finishes == '1,1': 
        result += ('Interior upgrades include potlights and crown mouldings. ')

if __name__ == "__main__":
    main()




