#!/usr/bin/python3
"""this script returns information about a given employee ID
TODO list progress using this REST API:
'https://jsonplaceholder.typicode.com'"""
import requests
import sys


if __name__ == "__main__":
    json_url = "https://jsonplaceholder.typicode.com/"

    employee_id = sys.argv[1]

    user_rsp = requests.get(json_url + "users/{}".format(employee_id))
    user = user_rsp.json()

    todo_rsp = requests.get(json_url + "todos", params={"userId": employee_id})
    todo_list = todo_rsp.json()

    total_tasks = len(todo_list)
    completed_tasks = sum(1 for task in todo_list if task['completed'])

    print("Employee {} is done with tasks ({}/{})".format(
        user['name'], completed_tasks, total_tasks) + ":")
    for task in todo_list:
        if task['completed']:
            print(f"\t{task['title']}")
