#!/usr/bin/python3
""" Python script that uses a REST API, and for a given employee IDi
returns information about their TODO list progress"""

import json
import requests
from sys import argv

if __name__ == "__main__":
    user = requests.get(
            'https://jsonplaceholder.typicode.com/users/')
    todo = requests.get(
            'https://jsonplaceholder.typicode.com/todos')
    line = []
    with open('todo_all_employees.json', 'w') as my_file:
        data = {}
        for item in todo.json():
            USER_ID = item.get('id')
            USERNAME = item.get('username')
            for task in todo.json():
                if task.get('userId') == USER_ID:
                    TASK_COMPLETED_STATUS = task.get('completed')
                    TASK_TITLE = task.get('title')
                    line.append({
                        "username": '{}'.format(USERNAME),
                        "task": '{}'.format(TASK_TITLE),
                        "completed": TASK_COMPLETED_STATUS})
            data[str(USER_ID)] = line
        json.dump(data, my_file)
