import config
from flask import Flask, request, Response
import json

app = Flask(__name__)


@app.route('/')
def greet():
    return 'Welcome to the to-do app'


@app.route('/task/new/', methods=['POST'])
def add_task():
    request_data = request.get_json()
    task = request_data['task']

    response_data = config.add_to_list(task)
    return response_data


# curl -X POST http://127.0.0.1:5000/task/new/ -d '{"task": "Go for grocery"}' -H 'Content-Type: application/json'

@app.route('/task/delete/', methods=['DELETE'])
def delete_task():
    request_data = request.get_json()
    task = request_data['task']

    response_data = config.remove_from_list(task)
    return response_data

# curl -X DELETE http://127.0.0.1:5000/task/delete/ -d '{"task": "Go for grocery"}' -H 'Content-Type: application/json'
