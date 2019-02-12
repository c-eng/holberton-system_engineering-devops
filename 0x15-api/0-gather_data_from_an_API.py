#!/usr/bin/python3
"""Gathers data from an api"""


from sys import argv
import requests

if __name__ == "__main__":
    r1 = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                      .format(argv[1]))
    r2 = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}"
                      .format(argv[1]))
    rson1 = r1.json()
    rson2 = r2.json()
    u_name = rson1.get("name")
    tasks = 0
    complete = 0
    complete_list = []
    for task in rson2:
        if task.get("completed"):
            complete += 1
            complete_list.append(task.get("title"))
        tasks += 1
    print("Employee {} is done with tasks({}/{}):".format(u_name, complete,
                                                          tasks))
    for task in complete_list:
        print("\t {}".format(task))
