from flask import Flask, request
from flask_cors import CORS
from json import dumps
from backend_functions import add_number
import sys
'''
default code
'''


def defaultHandler(err):
    response = err.get_response()
    print('response', err, err.get_response())
    response.data = dumps({
        "code": err.code,
        "name": "System Error",
        "message": err.get_description(),
    })
    response.content_type = 'application/json'
    return response


APP = Flask(__name__)
CORS(APP)


@APP.route("/join", methods=['POST'])
def post_add_number():
    info = request.get_json()

    return add_number(info['number'], info['postcode'])








if __name__ == '__main__':
    APP.run(port=(int(sys.argv[1]) if len(sys.argv) == 2 else 8080))