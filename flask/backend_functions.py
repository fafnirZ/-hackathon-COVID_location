
from database import get_data, get_total_cases
from datetime import datetime
import pandas as pd
import subprocess
'''
Database format:
[
    {'Postcode': 2010, 'Suburb': 'Hurstville', 'CaseCount': 3}
]

'''

def compare_lenghts():
    old = pd.get_csv("old.csv")
    oldlen = len(old)

    new = pd.get_csv("data.csv")
    newlen = len(new)

    if newlen > oldlen:
        #remove
        subprocess.call("bash remove_old.sh", shell=True)
        database.clear()
        date_data(stringy_date())

    else:
        database.clear()


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
        }
        database.append(new_postcode)

    return {}

#Function that given a date in the format 'YYYY-MM-DD', will return that day's data
def date_data(date):
    all_data = pd.read_csv("old.csv")
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

# Function that returns the current date data
def todays_data():
    now = datetime.now()
    date = now.strftime("%Y-%m-%d")
    return date_data(date)

    

