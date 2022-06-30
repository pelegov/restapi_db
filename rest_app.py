from flask import Flask, request
from datetime import datetime
import json
from db_connector import post_value, get_value, delete_value, put_value
app = Flask(__name__)


users = {}


#REST API Methods and GW definition
@app.route('/users/<user_id>', methods=['POST', 'GET', 'DELETE', 'PUT'])
def users(user_id):
    if request.method == 'GET':
        try:
            request_data = request.json
            user_id = request_data["user_id"]
            get_value(user_id)
            return {'user_id': user_id, 'user_name': users[user_id]}, 200 # status code
        except:
            return {'status': 'error', 'reason': 'no such ID'}, 500

    elif request.method == 'POST':
        try:
         #getting the json data payload from request
            request_data = request.json
            creation_date = current_time()
         #treating request_data as a dictionary to get a specific value from key
            user_name = request_data["user_name"]
            print(user_name)
            user_id = request_data["user_id"]
            print(user_id)
            post_value(user_id, user_name, creation_date)
            return {'user id': user_id, 'user name': user_name, 'status': 'saved'}, 200 # status code
        except:
            return {'status': 'error', 'reason': 'ID already exist'}, 500  # status code

    elif request.method == 'PUT':
        try:
            request_data = request.json
            user_name = request_data["user_id"]
            user_id = request_data["user_id"]
            put_value()
            return {'user id': user_id, 'user name': user_name, 'status': 'saved'}, 200  # status code
        except:
            return {'status': 'error', 'reason': 'no such ID'}, 500

    elif request.method == 'DELETE':
        try:
            request_data = request.json
            user_name = request_data["user_id"]
            delete_value(user_id)
            return {'user id': user_id, 'user name': user_name, 'status': 'saved'}, 200  # status code
        except:
            return {'status': 'error', 'reason': 'no such ID'}, 500

def current_time():
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')


app.run(host='127.0.0.1', debug=True, port=5000)


