from pynput.keyboard import Key, Controller
from datetime import datetime
from openpyxl import load_workbook

import time
# generate city and region for page3
def testing():
    new = string.split(" Transfer ")
    print(new)
    new2 = new[0].split(" $")
    print(new2)
    money = new2[1].replace(",",'')
    print(money)
def main():
    global string
    string = "Dec 15, 2017 $625,253 Transfer BHAT, POONAM SUSHIL; BHAT, SUSHILKUMAR PRI;"
    testing()



if __name__ == "__main__":
    main()


