from pynput.keyboard import Key, Controller
from datetime import datetime
from openpyxl import load_workbook

import time
# generate city and region for page3
def city_comment_gen():
    result = ""
    if city.title() == "Ottawa":
        result = "City of Ottawa;"
    elif city.title() == "Toronto":
        result = "City of Toronto;"
    elif city.title() == "Brampton":
        result = "Region of Peel; City of Brampton"
    elif city.title() == "Mississauga":
        result = "Region of Peel; City of Missisauga"
    elif city.title() == "Pickering":
        result = "Region of Durham; City of Missisauga"
    elif city.title() == "Oshawa":
        result = "Region of Durham; Town of Oshawa"
    elif city.title() == "Whitby":
        result = "Region of Durham; Town of Whitby"
    elif city.title() == "Ajax":
        result = "Region of Durham; Town of Ajax"
    elif city.title() == "Markham":
        result = "Region of York; City of Markham"
    elif city.title() == "Vaughan":
        result = "Region of York; City of Vaughan"
    return result
def main():
    global city
    city = "brampton"
    print (city_comment_gen())



if __name__ == "__main__":
    main()


