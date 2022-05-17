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
            'https://jsonplaceholder.typicode.com/todos/')
    with open('todo_all_employees.json', 'w') as my_file:
        data = {}
        for item in user.json():
            USER_ID = item.get('id')
            line = []
            for task in todo.json():
                if task.get('userId') == USER_ID:
                    line.append({
                        "username": item.get('username'),
                        "task": task.get('title'),
                        "completed": task.get('completed')})
            data[str(USER_ID)] = line
        json.dump(data, my_file)
