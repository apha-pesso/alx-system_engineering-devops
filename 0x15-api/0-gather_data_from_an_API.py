#!/usr/bin/python3
"""Module that Gather data from an API"""
import requests
from sys import argv


if __name__ == "__main__":
    todos = requests.get('https://jsonplaceholder.typicode.com/todos').json()
    total_todo = 0
    tasks_done = 0
    task_list = []
    for task in todos:
        if (task.get('userId') == int(argv[1])):
            total_todo += 1
            if (task.get('completed')):
                tasks_done += 1
                task_list.append(task.get('title'))
    users = requests.get('https://jsonplaceholder.typicode.com/users').json()
    for user in users:
        if (user.get("id") == int(argv[1])):
            emp_name = user.get('name')
    print("Employee {} is done with tasks({}/{}):".
          format(emp_name, tasks_done, total_todo))
    for t in task_list:
        print("\t {}".format(t))
