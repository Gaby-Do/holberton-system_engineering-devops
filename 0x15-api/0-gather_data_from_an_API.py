#!/usr/bin/python3
""" Python script that uses a REST API, and for a given employee IDi
returns information about their TODO list progress"""


import requests
from sys import argv

if __name__ == "__main__":
    user = requests.get(
            'https://jsonplaceholder.typicode.com/users/{}'.format(argv[1]))
    todo = requests.get(
            'https://jsonplaceholder.typicode.com/todos?userId={}'
            .format(argv[1]))
    EMPLOYEE_NAME = user.json().get('name')
    NUMBER_OF_DONE_TASKS = 0
    TOTAL_NUMBER_OF_TASKS = 0
    for item in todo.json():
        TOTAL_NUMBER_OF_TASKS = TOTAL_NUMBER_OF_TASKS + 1
        if item.get('completed') is True:
            NUMBER_OF_DONE_TASKS = NUMBER_OF_DONE_TASKS + 1
    print('Employee {} is done with tasks({}/{}):'.format(
        EMPLOYEE_NAME,
        NUMBER_OF_DONE_TASKS,
        TOTAL_NUMBER_OF_TASKS))
    for item in todo.json():
        if item.get('completed') is True:
            TASK_TITLE = item.get('title')
            print("\t {}".format(TASK_TITLE))
