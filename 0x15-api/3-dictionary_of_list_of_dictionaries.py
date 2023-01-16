#!/usr/bin/python3
"""Export data to csv file"""
import json
import requests
from sys import argv
from csv import writer, QUOTE_ALL

if __name__ == "__main__":
    users = requests.get('https://jsonplaceholder.typicode.com/users').json()
    todos = requests.get('https://jsonplaceholder.typicode.com/todos').json()
    full_dict = {}
    for user in users:
        emp_name = user.get('username')
        user_id = user.get('id')
        task_list = []
        for task in todos:
            if (task.get('userId') == user_id):
                tf = {"username": emp_name, "task": task.get('title'),
                      "completed": task.get('completed')}
                task_list.append(tf)
        full_dict[user_id] = task_list
        if (user_id == 5):
            print(task_list)

    file_name = "todo_all_employees.json"
    with open(file_name, 'w', encoding='utf-8') as f:
        # writer = writer(f, quoting=QUOTE_ALL)
        json.dump(full_dict, f)
