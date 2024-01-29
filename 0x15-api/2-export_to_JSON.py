#!/usr/bin/python3
"""this script returns information about a given employee ID
TODO list progress using this REST API:
'https://jsonplaceholder.typicode.com'
and export data in the JSON format."""
import json
import requests
import sys


if __name__ == "__main__":
    json_url = "https://jsonplaceholder.typicode.com/"

    employee_id = sys.argv[1]

    user_rsp = requests.get(json_url + "users/{}".format(employee_id))
    user = user_rsp.json()

    todo_rsp = requests.get(json_url + "todos", params={"userId": employee_id})
    todo_list = todo_rsp.json()

    json_f_name = "{}.json".format(employee_id)
    with open(json_f_name, 'w') as jsonfile:
        json.dump({employee_id: [
            {"task": task['title'],
             "completed": task['completed'],
             "username": user['name']} for task in todo_list
        ]}, jsonfile)
