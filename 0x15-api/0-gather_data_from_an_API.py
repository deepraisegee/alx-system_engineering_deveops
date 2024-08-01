#!/usr/bin/python3
""" """

import sys

import requests


def main():
    USER_ID = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com"

    # get employee data
    user = requests.get(f"{url}/users/{USER_ID}").json()

    # get the todos of the user
    todos = requests.get(f"{url}/todos", params={"userId": USER_ID}).json()

    completed = list(filter(lambda x: x["completed"], todos))

    print("Employee {} is done with tasks({}/{})".format(
                    user["name"], len(todos), len(completed)
                ))
    for todo in completed:
        print(f"\t{todo['title']}")


if __name__ == "__main__":
    main()
