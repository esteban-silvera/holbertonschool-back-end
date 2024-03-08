#!/usr/bin/python3
"""comments"""


import requests
from sys import argv


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    employee_id = int(argv[1])
    employee_data = requests.get(url + f'users/{employee_id}').json()
    employee_task = requests.get(url + f'users/{employee_id}/todos').json()

    completed_tasks = [task for task in employee_task if task["completed"]]

    print(f'Employee {employee_data["name"]} is done with ', end='')
    print(f'tasks({len(completed_tasks)}/{len(employee_task)}):')

    for task in completed_tasks:
        print('\t ' + task["title"])
