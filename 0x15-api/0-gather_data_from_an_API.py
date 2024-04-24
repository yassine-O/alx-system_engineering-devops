#!/usr/bin/python3

"""0. Gather data from an API"""

import requests
import sys

if __name__ == "__main__":
    id = sys.argv[1]
    r = requests.get(f'https://jsonplaceholder.typicode.com/users/{id}')
    employee = r.json()
    r = requests.get(f'https://jsonplaceholder.typicode.com/users/{id}/todos')
    todos = r.json()
    total = 0
    done = 0
    for task in todos:
        total += 1
        if task.get('completed'):
            done += 1
    name = employee.get('name')
    print(f"Employee {name} is done with tasks({done}/{total}):")
    for task in todos:
        if task.get('completed'):
            print(f"\t {task.get('title')}")
