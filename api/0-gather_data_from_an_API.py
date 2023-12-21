#!/usr/bin/python3
import requests

def todo_list_progress(task_id):
    # Fetch task data
    task_response = requests.get(f'https://jsonplaceholder.typicode.com/todos/{task_id}')
    task_data = task_response.json()

    # Fetch user data
    user_response = requests.get(f'https://jsonplaceholder.typicode.com/users/{task_data["userId"]}')
    user_data = user_response.json()
    employee_name = user_data['name']

    # Check if the task is completed
    is_completed = task_data['completed']
    task_title = task_data['title']

    # Print task details
    print(f'Employee {employee_name} has the task "{task_title}" with ID {task_id}.')
    print('Task status: Completed' if is_completed else 'Task status: Not completed')

# Test the function with an example task ID
todo_list_progress(1)
