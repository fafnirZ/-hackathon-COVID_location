
from database import get_data, get_total_cases
from datetime import datetime
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

#Function that given a date in the format 'YYYY-MM-DD', will return that day's data
def date_data(date):
    all_data = pd.read_csv("scraper/data.csv")
    day_data = all_data.loc[all_data['notification_date'] == date]
    formatted = []
    for case in day_data.itertuples():
        suburb = case.lga_name19
        postcode = case.postcode
        suburb_exists = False
        for area in formatted:
            if area['Suburb'] == suburb:
                suburb_exists = True
                area['CaseCount'] += 1
        if not suburb_exists:
            new_suburb = {
                'Postcode': postcode,
                'Suburb': suburb,
                'CaseCount': 1
            }
            formatted.append(new_suburb)
    return formatted

# Function that returns the current date into the correct format for date_data
def stringify_date():
    now = datetime.now()
    return now.strftime("%Y-%m-%d")
