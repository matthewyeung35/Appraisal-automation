from pynput.keyboard import Key, Controller
from datetime import datetime
from openpyxl import load_workbook

import time
# generate city and region for page3
def testing():
    new_string = string.split(" Transfer ")
    print(new_string)
    geo_name = new_string[1]
    new_string = new_string[0].split(" $")
    geo_date = new_string[0]
    geo_price = new_string[1].replace(",",'')
def main():
    global string
    string = "Dec 15, 2017 $625,253 Transfer BHAT, POONAM SUSHIL; BHAT, SUSHILKUMAR PRI;"
    testing()



if __name__ == "__main__":
    main()


