#!/usr/bin/python3

"""0. Gather data from an API"""

import requests
import sys

if __name__ == "__main__":
    id = sys.argv[1]
    url = f'https://jsonplaceholder.typicode.com/users/{id}'
    employee = requests.get(url).json()
    url = f'https://jsonplaceholder.typicode.com/users/{id}/todos'
    todos = requests.get(url).json()
    data = ""
    userId = employee.get('id')
    username = employee.get('username')
    for task in todos:
        status = task.get('completed')
        title = task.get('title')
        data += f'"{userId}","{username}","{status}","{title}"\n'
    with open(f'{userId}.csv', 'w') as file:
        file.write(data)
