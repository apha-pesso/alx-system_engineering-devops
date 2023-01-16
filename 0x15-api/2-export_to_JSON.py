#!/usr/bin/python3
"""Export data to csv file"""
import requests
from sys import argv
from csv import writer, QUOTE_ALL
import json

if __name__ == "__main__":
    users = requests.get('https://jsonplaceholder.typicode.com/users').json()
    for user in users:
        if (user.get("id") == int(argv[1])):
            emp_name = user.get('username')
    todos = requests.get('https://jsonplaceholder.typicode.com/todos').json()
    task_list = []
    for task in todos:
        if (task.get('userId') == int(argv[1])):
            tf = {"task": task.get('title'), "completed":
                  task.get('completed'), "username": emp_name}
            task_list.append(tf)

    file_name = "{}.json".format(argv[1])
    with open(file_name, 'w', encoding='utf-8') as f:
        # writer = writer(f, quoting=QUOTE_ALL)
        json.dump({argv[1]: task_list}, f)
