#!/usr/bin/python3
"""Export data to csv file"""
import requests
from sys import argv
from csv import writer, QUOTE_ALL

if __name__ == "__main__":
    todos = requests.get('https://jsonplaceholder.typicode.com/todos').json()
    task_list = []
    for task in todos:
        if (task.get('userId') == int(argv[1])):
            task_list.append(task)

    users = requests.get('https://jsonplaceholder.typicode.com/users').json()
    for user in users:
        if (user.get("id") == int(argv[1])):
            emp_name = user.get('username')

    file_name = "{}.csv".format(argv[1])
    with open(file_name, 'w', newline='', encoding='utf-8') as f:
        writer = writer(f, quoting=QUOTE_ALL)

        for task in task_list:
            writer.writerow([argv[1], emp_name, task.get('completed'),
                            task.get('title')])
