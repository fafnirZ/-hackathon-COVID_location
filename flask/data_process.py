from database import database, get_data
import numpy as np
import pandas as pd

data = pd.read_csv("data.csv")



def in_data(row, database):
    if len(database) == 0:
        return False
    
    else:
        for data in database:
            if data['Postcode'] == row.postcode:
                return True

        return False

def insert_data(row, database):
    database.append({
        'Postcode' : row.postcode,
        'Phone Numbers' : [],
        'Suburb' : [{
            'Suburb name': row.lga_name19,
            'Cumulative Cases' : 1,
            'New Cases' : 0,
        }]
        
    })


def insert_all(row, database):
	for row in data.itertuples():
    if not in_data(row, database):
        insert_data(row, database)