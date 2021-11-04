import os, sys
from flask import Flask, request
from flask_cors import CORS

for path in ['config', 'controllers']:
    sys.path.append(os.path.join(os.path.dirname(__file__), path))

from dbConfig import createDB
from UsersController import getUsers, addUser

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['POST', 'GET'])
def index():
    
    if request.method == 'GET':

        return getUsers()

    elif request.method == 'POST':

        data = request.json

        if type(data['id']) == int and data['first'].isalpha() and data['last'].isalpha():
            return addUser(data['id'], data['first'], data['last'])

        else:
            return { 'message': 'Invalid input!', 'Error': True }

    else:

        app.register_error_handler(405, 'Method Not Allowed')
        return { 'Error': 'Method Not Allowed', 'Code': 405 }

def main():

    createDB()
    app.run(host='localhost', port=5000, debug=False)

if __name__ == '__main__':

    main()