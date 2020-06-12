
'''
Database format:
{
    postcode: {
        'Phone Numbers': [list of numbers]
        'Number of Active Cases': {'Suburb': , 'Suburb': }
        'New Active Cases': [list of suburbs with new active cases in the most recent pull of data]}
}

'''

database = {}


def add_number(number, postcode):
    database[postcode]['Phone Numbers'].append(number)
    return {}

def add_suburb()
    database
def update()



if __name__ == "__main__":
    add_number('0413843630', 2036)

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