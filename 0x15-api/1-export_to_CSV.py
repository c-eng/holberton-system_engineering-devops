#!/usr/bin/python3
"""Gathers data from an api"""


import csv
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
    output = [{"id": argv[1], "name": u_name,
               "completed": task.get("completed"), "title": task.get("title")}
              for task in rson2]
    k = ["id", "name", "completed", "title"]
    with open("{}.csv".format(argv[1]), "w") as outfile:
        writer = csv.DictWriter(outfile, k, quoting=csv.QUOTE_ALL)
        writer.writerows(output)
