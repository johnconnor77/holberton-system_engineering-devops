#!/usr/bin/python3
"""
    Python script that returns information about a persons
    To Do list when the employee ID is given
"""

import requests
from sys import argv


def get_todolist_progress():
    """
    Get's the  to do list progress of a specified user
    """
    user_id = argv[1]
    url = "https://jsonplaceholder.typicode.com/"

    user_info = requests.get(url + "users/{}"
                             .format(user_id)).json()
    total_user_tasks = requests.get(url + "todos?userId={}"
                                    .format(user_id)).json()
    completed_user_tasks = requests.get(url + "todos?userId={}&&completed=true"
                                        .format(user_id)).json()

    try:
        print("Employee {} is done with tasks({}/{}):"
              .format(user_info.get('name'),
                      len(completed_user_tasks), len(total_user_tasks)))

        for task in completed_user_tasks:
            print("\t {}".format(task.get("title")))
    except KeyError:
        pass


if __name__ == "__main__":
    get_todolist_progress()
