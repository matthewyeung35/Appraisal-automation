from openpyxl import load_workbook, Workbook
# for adding , and for multiple faciltiies
def facilities_format(facilities):
    if ownership == '0':
        if ',' in facilities:
            x = facilities.split(',')
            i = 0
            result = ''
            while i < len(x):
                if i == 0:
                    result += (', ') + x[i]
                elif i != len(x)-1:
                    result += (',') + x[i]
                else:
                    result += (' and') + x[i]
                i += 1
            return result
        else:
            return (' and ') + facilities
    else:
        return facilities
        
def main():
    global ownership
    ownership = '0'
    facilities1 = 'River Mist Park, St Benedict School, x park'
    print(facilities_format(facilities1))
if __name__ == "__main__":
    main()

