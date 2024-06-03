#!/usr/bin/python3

"""0. Gather data from an API"""

import json
import requests
import sys

if __name__ == "__main__":
    id = sys.argv[1]
    url = f'https://jsonplaceholder.typicode.com/users/{id}'
    employee = requests.get(url).json()
    url = f'https://jsonplaceholder.typicode.com/users/{id}/todos'
    todos = requests.get(url).json()
    tasks = []
    name = employee.get('name')
    for todo in todos:
        task = {"task": todo.get('title'),
                "completed": todo.get('completed'),
                "username": name}
        tasks.append(task)
    user_tasks = {id: tasks}
    with open(f'{id}.json', 'w') as file:
        json.dump(user_tasks, file)
