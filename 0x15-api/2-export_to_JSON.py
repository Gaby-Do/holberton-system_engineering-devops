#!/usr/bin/python3
""" Python script that uses a REST API, and for a given employee IDi
returns information about their TODO list progress"""

import json
import requests
from sys import argv

if __name__ == "__main__":
    user = requests.get(
            'https://jsonplaceholder.typicode.com/users/{}'.format(argv[1]))
    todo = requests.get(
            'https://jsonplaceholder.typicode.com/todos?userId={}'
            .format(argv[1]))
    USER_ID = user.json().get('id')
    USERNAME = user.json().get('username')
    line = []
    for item in todo.json():
        TASK_COMPLETED_STATUS = item.get('completed')
        TASK_TITLE = item.get('title')
        row = {
                "task": '{}'.format(TASK_TITLE),
                "completed": '{}'.format(TASK_COMPLETED_STATUS),
                "username": '{}'.format(USERNAME)}
        line.append(row)
    data = {"{}".format(USER_ID): line}
    with open('{}.json'.format(USER_ID), 'w') as my_file:
        json.dump(data, my_file)
