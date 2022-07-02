from flask import Flask, request
from db_connector import get_value
import requests
app = Flask(__name__)

@app.route('/users/get_user_data/<user_id>', methods=['GET'])
def get_user_name(user_id):
    ### Creating value based on function retur values in http convention.
        user_name = get_value(user_id)
        if user_name:
            return "<H1 id='user'>" + user_name + "</H1>"
        else:
            return "<H1 id='error'>" 'no such user: ' + user_id + "</H1>"
app.run(host='127.0.0.1', debug=True, port=5001)