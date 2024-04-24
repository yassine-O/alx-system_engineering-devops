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
    total = 0
    done_tasks = []
    for task in todos:
        total += 1
        if task.get('completed'):
            done_tasks.append(task)
    name = employee.get('name')
    done = len(done_tasks)
    print(f"Employee {name} is done with tasks({done}/{total}):")
    for task in done_tasks:
        print(f"\t {task.get('title')}")
