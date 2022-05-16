#!/usr/bin/python3
""" Python script that uses a REST API, and for a given employee IDi
returns information about their TODO list progress"""

import csv
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
    with open('{}.csv'.format(USER_ID), 'w') as my_file:
        writer = csv.writer(my_file, quoting=csv.QUOTE_ALL)
        for item in todo.json():
            TASK_COMPLETED_STATUS = item.get('completed')
            TASK_TITLE = item.get('title')
            line = ['{}'.format(USER_ID),
                    '{}'.format(USERNAME),
                    '{}'.format(TASK_COMPLETED_STATUS),
                    '{}'.format(TASK_TITLE)]
            writer.writerow(line)
