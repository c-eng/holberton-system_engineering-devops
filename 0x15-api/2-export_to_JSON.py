#!/usr/bin/python3
"""Gathers data from an api"""


import json
import requests
from sys import argv

if __name__ == "__main__":
    r1 = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                      .format(argv[1]))
    r2 = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}"
                      .format(argv[1]))
    rson1 = r1.json()
    rson2 = r2.json()
    u_name = rson1.get("username")
    output = {"{}".format(argv[1]): [{"task": task.get("title"),
                                      "completed": task.get("completed"),
                                      "username": u_name}
              for task in rson2]}
    with open("{}.json".format(argv[1]), "w") as outfile:
        json.dump(output, outfile)
