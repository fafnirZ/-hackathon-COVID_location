
from database import get_data, get_total_cases
import datetime
import pandas as pd

'''
Database format:
[
    {
        'Postcode': postcode,
        'Phone Numbers': [list of numbers],
        'Suburb': [
            {
                'Suburb Name': ,
                'New Cases': ,
                'Cumulative Cases': ,
            }
        ]
        
    },
]

'''

def add_number(number, postcode):
    database = get_data()
    postcode_exists = False
    for area in database:
        if area['Postcode'] is postcode:
            postcode_exists = True
            area['Phone Numbers'].append(number)
            break
    if postcode_exists is False:
        new_postcode = {
            'Postcode': postcode,
            'Phone Numbers': [number],
            'Suburb':[]
        }
        database.append(new_postcode)

    return {}

# ==== OLD FUNCTIONS ====

# Use this function to clear new cases for all suburbs before adding the newest iteration 
def clear_new_active():
    database = get_data()
    for area in database:
        for places in area['Suburb']:
            places['New Cases'] = 0

def suburb_in_postcode(area, suburb):
    for places in area['Suburb']:
        if places['Suburb Name'] is suburb:
            return True
    return False

# 
# Function that updates database for all new cases since previous run
def update_active_cases():
    database = get_data()
    daily_cases = extract_daily()
    for case in daily_cases.itertuples():
        suburb = case.lga_name19
        print(suburb)
        postcode = case.postcode
        postcode_exists = False
        for area in database:
            if area['Postcode'] == postcode:
                postcode_exists = True
                suburb_exists = False
                for place in area['Suburb']:
                    if place['Suburb Name'] == suburb:
                        suburb_exists = True
                        place['New Cases'] += 1
                        place['Cumulative Cases'] += 1
                if not suburb_exists:
                    new_suburb = {
                        'Suburb Name': suburb,
                        'New Cases': 1,
                        'Cumulative Cases': 1
                    }
                    area['Suburb'].append(new_suburb)
        if not postcode_exists:
            new_postcode = {
                'Postcode': postcode,
                'Phone Numbers': [],
                'Suburb': [{'Suburb Name': suburb, 'New Cases': 1, 'Cumulative Cases': 1}]
            }
            database.append(new_postcode)

# Function that reads only the new daily data from csv as well as update the total number of cases
def extract_daily():
    total_cases = get_total_cases()
    data = pd.read_csv("scraper/testdata.csv", skiprows=range(1,(total_cases+1)))

    num_new_cases = pd.Index(data).size
    total_cases += num_new_cases
    return data
#Date as a string in format '2020-03-19'
def extract_date(date):


def extract_initial():
    total_cases = get_total_cases()
    data = pd.read_csv("scraper/testdata.csv")

    num_new_cases = pd.Index(data).size
    total_cases += num_new_cases
    return data

if __name__ == '__main__':
    print(get_data())
    # add_number('0413843630', 2036)
    update_active_cases()
    
    print(get_total_cases())
    print(get_data())
    print(get_total_cases())
    clear_new_active()
    print(get_data())
