
'''
Database format:
{
    postcode: {
        'Phone Numbers': [list of numbers]
        'Active Cases': }
}

'''

database = {}


def add_number(number, suburb):
    database[suburb].append(number)
    return {}

def add_suburb()
    
def update()








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