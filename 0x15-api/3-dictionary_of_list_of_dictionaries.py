#!/usr/bin/python3

"""0. Gather data from an API"""

import json
import requests

if __name__ == "__main__":
    emp_url = 'https://jsonplaceholder.typicode.com/users/'
    todos_url = f'https://jsonplaceholder.typicode.com/todos'
    todos = requests.get(todos_url).json()
    user_tasks = {}
    for todo in todos:
        userId = todo.get('userId')
        employee = requests.get(emp_url + str(userId)).json()
        name = employee.get('username')
        task = {"task": todo.get('title'),
                "completed": todo.get('completed'),
                "username": name}
        user_tasks.setdefault(str(userId), []).append(task)
    with open('todo_all_employees.json', 'w') as file:
        json.dump(user_tasks, file)
