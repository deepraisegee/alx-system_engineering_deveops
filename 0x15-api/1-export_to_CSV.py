#!/usr/bin/python3
""" Get todo information of a given user id """

import csv
import requests
import sys


def main():
    USER_ID = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com"

    # get employee data
    user = requests.get(f"{url}/users/{USER_ID}").json()

    # get the todos of the user
    todos = requests.get(f"{url}/todos", params={"userId": USER_ID}).json()

    completed = list(filter(lambda x: x["completed"], todos))

    print("Employee {} is done with tasks({}/{}):".format(
                    user["name"], len(completed), len(todos)
                ))
    [print(f"\t {todo['title']}") for todo in completed]

    # write to csv
    with open(f"{USER_ID}.csv", "w") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [writer.writerow(
            [USER_ID, user["name"], todo["completed"], todo["title"]]
        ) for todo in todos]


if __name__ == "__main__":
    main()
