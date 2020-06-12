
'''
Database format:
[
    {
        'Postcode': postcode,
        'Phone Numbers': [list of numbers],
        'Suburb': {
            'New Cases': ,
            'Cumulative Cases': ,
        }
        
    },
]

'''

global database 
database = []


# ==== ANALYTIC FUNCTIONS ====




# ==== DATABASE FUNCTIONS ====

# ASSUME: All valid postcodes are already in database? Or add
def add_number(number, postcode):
    postcode_exists = False
    for area in database:
        if area['Postcode'] is postcode:
            postcode_exists = True
            area['Phone Numbers'].append(number)
            break
    if postcode_exists is False:
        new_postcode = {
            'Postcode': postcode,
            'Phone Numbers': [number]
        }
        database.append(new_postcode)

    return {}


# JACKY IS WRITING THIS
# def add_new_case(suburb):
#     # database['New Active Cases'].append(suburb)
#     if suburb not in database['New Active Cases']:
#         database['New Active Cases'].append(suburb)


# Use this function to clear new cases for all suburbs before adding the newest iteration 
def clear_new_active():
    for area in database:
        for suburb in area.keys():
            if suburb is not 'Phone Numbers' or 'Postcode':
                area[suburb]['New Cases'] = 0

def update_active_cases(daily_data):
    for case in daily_data:
        suburb = case[5]
        postcode = case[1]
        postcode_exists = False
        for area in database:
            if area['Postcode'] is postcode:
                postcode_exists = True
                if suburb in area.keys():
                    area[suburb]['New Cases'] += 1
                    area[suburb]['Cumulative Cases'] += 1
                else:
                    area[suburb]['New Cases'] = 1
                    area[suburb]['Cumulative Cases'] = 1
        if not postcode_exists:
            new_postcode = {
                'Postcode': postcode,
                'Phone Numbers': [],
                suburb: {'New Cases': 1, 'Cumulative Cases': 1}
            }
            database.append(new_postcode)


if __name__ == '__main__':
    add_number('0413843630', 2036)
    daily_data = [['2020-06-11', 2144.0, 'X740', 'Western Sydney', 12380.0,
        'Cumberland (A)']]
    update_active_cases(daily_data)
    print(database)

# from flask import Flask
# APP = Flask(__name__)


# @APP.route("/")
# def hello():
#     return "hello"


# if __name__ == "__main__":
#     PORT = int(sys.argv[1]) if len(sys.argv) == 2 else 8080
#     #set_port(PORT)
#     APP.run(port=PORT)
#     #stop_saving()