#!/usr/bin/python3
"""this script returns information about a given employee ID
TODO list progress using this REST API:
'https://jsonplaceholder.typicode.com'
and export data in the CSV format"""
import csv
import requests
import sys


if __name__ == "__main__":
    json_url = "https://jsonplaceholder.typicode.com/"

    employee_id = sys.argv[1]

    user_rsp = requests.get(json_url + "users/{}".format(employee_id))
    user = user_rsp.json()

    todo_rsp = requests.get(json_url + "todos", params={"userId": employee_id})
    todo_list = todo_rsp.json()

    username = user.get("username")

    csv_file_name = "{}.csv".format(employee_id)

    with open(csv_file_name, 'w', newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)

        for task in todo_list:
            writer.writerow([
                employee_id,
                username,
                task.get("completed"),
                task.get("title")])
