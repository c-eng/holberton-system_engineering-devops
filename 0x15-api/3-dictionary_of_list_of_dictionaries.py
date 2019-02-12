#!/usr/bin/python3
"""Gathers data from an api"""


import json
import requests

if __name__ == "__main__":
    r1 = requests.get("https://jsonplaceholder.typicode.com/users")
    user_list = []
    for user in r1.json():
        user_list.append((user.get("id"), user.get("username")))
    output = []
    for user in user_list:
        r2 = requests.get("https://jsonplaceholder.typicode.com/" +
                          "todos?userId={}".format(user[0]))
        rson2 = r2.json()
        output.append({"{}".format(user[0]):
                       [{"task": task.get("title"),
                         "completed": task.get("completed"),
                         "username": user[1]}
                        for task in rson2]})
    with open("todo_all_employees.json", "w") as outfile:
        json.dump(output, outfile)
